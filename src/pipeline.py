
import os
import fnmatch
import re
import subprocess
import sys
import json
import imp
import time
from pprint import pprint

lib_path = os.path.abspath(os.path.join('drmaa-python'))
sys.path.append(lib_path)
import drmaa

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
        self.logHandler = open(self.setting['config']['log']+"/jid_list", "w+")
        self.logger("Start pipeline")

    def processApp(self):
        self.logger("processApp")

    def pj_initialize(self):
        self.logger("initialize")

    def _add_env(self, env_vars):
        self.environment = {}
        for env_var, value in env_vars.items():
            try:
                if not isinstance(env_var, bytes):
                    env_var = env_var.encode()
                if not isinstance(value, bytes):
                    value = value.encode()
            except UnicodeEncodeError:
                print "exception"
            else:
                self.environment[env_var] = value

    def run(self):
        for step in self.setting['step']:
            mod = __import__(step["packageName"])
            if hasattr(mod, step["className"]):
                self._add_env(os.environ)
                with drmaa.Session() as s:
                        jt = s.createJobTemplate()
                        jt.jobName = "drmaa-job"
                        jt.errorPath = ":"+os.path.join(os.getcwd(), "log", 'GG.oge_err.log')
                        jt.outputPath = ":"+os.path.join(os.getcwd(), "log", 'GG.oge_out.log')
                        jt.nativeSpecification = "-q hipipe.q -V -cwd" 
                        jt.jobEnvironment = self.environment
                        jt.remoteCommand = sys.executable
                        jt.args = ['-m', step["className"]]
                        jobid = s.runJob(jt)
                        print('Your job has been submitted with ID %s' % jobid)
                        print('Job stats is '+s.jobStatus(jobid))
                        print('Cleaning up')
                        self.logHandler.write("JID-"+step["packageName"]+"-"+step["className"]+":"+jobid+"\n")
                        self.logHandler.flush()
                        s.deleteJobTemplate(jt)
        self.logHandler.close()
