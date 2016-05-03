#!/usr/bin/python
from time import sleep
from piglow import PiGlow

piglow = PiGlow()

for i in range(1, 100):
  #on
  piglow.arm(1,100)
  sleep(0.5)
  piglow.arm(2,100)
  sleep(0.5)
  piglow.arm(3,100)
  sleep(0.5)
  #off
  piglow.arm(1,0)
  sleep(0.5)
  piglow.arm(2,0)
  sleep(0.5)
  piglow.arm(3,0)
  sleep(0.5)
