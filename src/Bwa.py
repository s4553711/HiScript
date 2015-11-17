import time
import sys
import subprocess
import task

class Bwa(task.taskDef):
    def __init__(self):
        super(Bwa, self).__init__()
                            
    def run(self):
        super(Bwa, self).run()
        print "I am "+self.name
        try:
            cmd = ["pwd"]
            p = subprocess.Popen(cmd, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)

            while True:
                out = p.stdout.readline()
                if out == '' and p.poll() != None:
                    break
                if out != '':
                    print "TT> "+out.rstrip()
                    sys.stdout.flush()

            p.communicate()
            if p.poll() >= 1:
                print "ERROR"
                return

        except Exception as ins:
            print "ERROR > ",sys.exc_info()
            print "ERROR > ",type(ins)
            print "ERROR > ",ins.args
