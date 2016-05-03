#!/usr/bin/python
from time import sleep
from piglow import PiGlow

piglow = PiGlow()

for i in range(1 100):
  #on
  piglow.arm(0,100)
  time.sleep(0.5)
  piglow.arm(1,100)
  time.sleep(0.5)
  piglow.arm(2,100)
  time.sleep(0.5)
  #off
  piglow.arm(0,0)
  time.sleep(0.5)
  piglow.arm(1,0)
  time.sleep(0.5)
  piglow.arm(2,0)
  time.sleep(0.5)
