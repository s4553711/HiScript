
import os
import fnmatch
import re
import subprocess
import sys
import json
import imp
import time
from pprint import pprint

class pipeline(object):
    def __init__(self):
        self.name = ''
        self.taskId = ''
        self.taskPath = ''
        self.scriptPath = ''
        self.inputPath = ''
        self.outputPath = ''
        self.setting = ''

    def logger(self, message):
        print("["+time.strftime('%Y-%m-%d %H:%M%p %Z')+"] "+message)

    def read_config(self):
        with open("app.json") as json_file:
            self.setting = json.load(json_file)

    def clean(self):
        self.read_config()
        self.logger("Start pipeline")

    def processApp(self):
        self.logger("processApp")

    def pj_initialize(self):
        self.logger("initialize")

    def run(self):
        for step in self.setting['step']:
            mod = __import__(step["packageName"])
            if hasattr(mod, step["className"]):
                class_inst = getattr(mod, step["className"])()
                class_inst.setName(step['name'])
                class_inst.init()
                class_inst.run()
                class_inst.finish()
