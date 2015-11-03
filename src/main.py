#!/usr/bin/python
import os
import task
import sys
import QC

print "Log> Job Start"
q = QC.QC()
q.setName("task-sample")
q.init()
q.run()
q.finish()
