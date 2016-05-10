#!/usr/bin/python
from time import sleep
from piglow import PiGlow

piglow = PiGlow()
piglow.all(0)
# construction
for i in range(1, 20):
  piglow.orange(100)
  sleep(.5)
  piglow.all(0) 
  piglow.yellow(100)
  sleep(.5)
  piglow.all(0) 

