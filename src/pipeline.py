
import os
import fnmatch
import re
import subprocess
import sys
import json
import imp

class pipeline(object):
    def __init__(self):
        self.name = ''
        self.taskId = ''
        self.taskPath = ''
        self.scriptPath = ''
        self.inputPath = ''
        self.outputPath = ''
        self.setting = ''

    def read_config(self):
        with open("app.json") as json_file:
            self.setting = json.load(json_file)
            print(self.setting['apps'][0])

    def clean(self):
        self.read_config()
        print "Start pipeline"

    def processApp(self):
        print "processApp"

    def pj_initialize(self):
        print "initialize"

    def run(self):
        for step in self.setting['step']:
            mod = imp.load_source(step["packageName"], './')
            if hasattr(mod, step["className"]):
                class_inst = getattr(mod, step["className"])()
                class_inst.setName('QC-Job')
                class_inst.init()
                class_inst.run()
                class_inst.finish()
