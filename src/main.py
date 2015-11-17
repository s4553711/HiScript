#!/usr/bin/python
import os
import task
import sys
import pipeline
#import QC
#import Bwa

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
