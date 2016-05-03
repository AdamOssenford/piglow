#!/usr/bin/python
from time import sleep
from piglow import PiGlow

piglow = PiGlow()
# the police
for i in range(1, 100):
  piglow.blue(100)
  sleep(.1)
  piglow.red(100)
  sleep(.1)
