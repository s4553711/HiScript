#!/usr/bin/python
import os
import task
import sys
import pipeline
#import QC
#import Bwa
lib_path = os.path.abspath(os.path.join('drmaa-python'))
sys.path.append(lib_path)
import drmaa

p = pipeline.pipeline();
p.clean()
p.processApp()
p.pj_initialize()
p.run()

#print "Log> Job Start"
#q = TT.TT()
#q.setName("TT task-sample")
#q.init()
#q.run()
#q.finish()
