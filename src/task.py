import os
import fnmatch
import re
import subprocess
import time
import sys

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

    def init(self):
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

    def run(self):
        runCheckResult = self.holdJob()
        if runCheckResult:
            self.logger("Job start")
            print "Run job"

    def finish(self):
        self.logger("Job finish")
        print "Finish job"
