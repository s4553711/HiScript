import os
import fnmatch
import re
import subprocess
import time
import json
import sys

lib_path = os.path.abspath(os.path.join('drmaa-python'))
sys.path.append(lib_path)
import drmaa

class taskDef(object):
    def __init__(self):
        self.jobId = ""
        self.name = ''
        self.queue = ''
        self.scriptPath = ''
        self.taskPath = ''
        self.inputPath = ''
        self.outputPath = ''
        self.prevStateLog = ''
        self.setting = ''
		
    def setName(self, name):
        self.name = name

    def setJobId(self, id):
        self.jobId = id

    def setQueue(self, queue):
        self.queue = queue

    def setScriptPath(self, path):
        self.scriptPath = path

    def setTaskPath(self, path):
        self.taskPath = path

    def setInputPath(self, path):
        self.inputPath = path

    def setOutputPath(self, path):
        self.outputPath = path
	
    def setPrevStateLog(self,input):
        self.prevStateLog = input
	
    def setCurrentStateLog(self,input):
        self.currentStateLog = input

    def setLogFolder(self, input):
        self.logPath = input

    def read_config(self):
        with open("app.json") as json_file:
            self.setting = json.load(json_file)
        for step in self.setting['step']:
            if self.__class__.__name__ == step['className']:
                self.settingObj = step

    def init(self):
        self.read_config()
        self.setName(self.settingObj['name'])
        self.setCurrentStateLog(self.settingObj['logName'])
        if "logFolder" in self.settingObj:
            self.setLogFolder(os.path.join(self.setting['config']['log'], self.settingObj['logFolder']))
        else:
            self.setLogFolder(self.setting['config']['log'])
        self.initLog()

    def initLog(self):
        if not os.path.isdir(self.logPath):
            os.makedirs(self.logPath)
        self.logHandle = open(self.logPath+"/"+self.currentStateLog, "w+")

    def logger(self, message):
        self.logHandle.write("["+time.strftime('%Y-%m-%d %H:%M%p %Z')+"] "+message+"\n")
        self.logHandle.flush()

    def checkStatus(self,fileName):
        pattern = re.compile(".*?error|.*?stop")
        status = "normal"
        f = open(fileName,"r");
        for line in f:
            if pattern.match(line.strip()):
                status = "error"
                return status
        return status

    def holdJob(self):
        if self.prevStateLog == "":
            return True
        if os.path.isdir(self.logPath):
            for file in os.listdir(self.logPath):
                if fnmatch.fnmatch(file,os.path.basename(self.prevStateLog)):
                    state = self.checkStatus(self.logPath+"/"+file)
                    if state == "error" or state == "stop": 
                        return False
        return True

    def pipeline_run(self):
        self.init()
        print "pipeline run"
        self.run()
        self.finish()

    def runOge(self):
        print "run by oge"
        with drmaa.Session() as s:
            jt = s.createJobTemplate()
            jt.jobName = "drmaa-job"
            jt.errorPath = ":"+os.path.join(os.getcwd(), self.logPath, self.name+'.oge_out.log')
            jt.outputPath = ":"+os.path.join(os.getcwd(), self.logPath, self.name+'.oge_err.log')
            jt.remoteCommand = os.path.join(os.getcwd(), 'sleeper.sh')
            jt.nativeSpecification = "-q " + self.queue
            jt.args = ['30', 'Google said:']

            jobid = s.runJob(jt)
            print('Your job has been submitted with ID %s' % jobid)
            print ('Job stats is '+s.jobStatus(jobid))
            print('Cleaning up')
            s.deleteJobTemplate(jt)

    def run(self):
        runCheckResult = self.holdJob()
        if runCheckResult:
            self.logger("Job start")
            print "Run job"

    def finish(self):
        self.logger("Job finish")
        print "Finish job"
