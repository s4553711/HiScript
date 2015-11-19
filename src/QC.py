import time
import sys
import subprocess
import task

class QC(task.taskDef):
    def __init__(self):
        super(QC, self).__init__()
                            
    def run(self):
        super(QC, self).run()
        try:
            cmd = ["ls", "-al"]
            p = subprocess.Popen(cmd, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)

            while True:
                out = p.stdout.readline()
                if out == '' and p.poll() != None:
                    break
                if out != '':
                    print "> "+out.rstrip()
                    super(QC, self).logger(out.rstrip())
                    sys.stdout.flush()

            p.communicate()
            if p.poll() >= 1:
                print "ERROR"
                return

        except Exception as ins:
            print "ERROR > ",sys.exc_info()
            print "ERROR > ",type(ins)
            print "ERROR > ",ins.args
