import os
import fnmatch
import re
import subprocess
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
        print "Task Initialization"

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
        status = True
        if self.prevStateLog == "":
            return status
        for file in os.listdir(self.logPath):
            if fnmatch.fnmatch(file,os.path.basename(self.prevStateLog)):
                state = self.checkStatus(self.logPath+"/"+file)
                if state == "error" or state == "stop": 
                    status = False
                    return status
        return status

    def run(self):
        runCheckResult = self.holdJob()
        if runCheckResult:
            print "Run job"

    def finish(self):
        print "Finish job"
