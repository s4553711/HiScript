import os;
import sys;
sys.path.append(os.getcwd()+"/src")
import pipeline;
import task;

def main(args):
    print(u'OK Lets GO');
    print(args)

if __name__ == '__main__':
    main(sys.argv)
    p = pipeline.pipeline();
    p.clean()
    p.processApp()
    p.pj_initialize()
    #p.run()
