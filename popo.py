#!/usr/bin/python
from time import sleep
from piglow import PiGlow

piglow = PiGlow()
piglow.all(0)
# the police
for i in range(1, 100):
  piglow.blue(100)
  sleep(.2)
  piglow.red(100)
  sleep(.2)
