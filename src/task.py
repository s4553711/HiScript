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

    def init(self):
        print "Task Initialization"

    def run(self):
        print "Run job"

    def finish(self):
        print "Finish job"
