# -*- coding: utf-8 -*-
import time
f = open('power.txt')
line = f.readline()
while line:
    print (line),
    time.sleep(2)
    line = f.readline()
f.close()