#!/usr/bin/python
from time import sleep
from piglow import PiGlow

piglow = PiGlow()
piglow.all(0)
# the police
for i in range(1, 20):
  piglow.all(0)
  piglow.blue(100)
  sleep(.2)
  piglow.all(0) 
  piglow.red(100)
  sleep(.2)

piglow.all(0)
piglow.all(200)
piglow.all(0)
