#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep
from itertools import product

GPIO.setmode(GPIO.BCM)

gpios = [26, 19, 13, 6] # 5 (not active)
leds = [] # blue, green, yellow, red, white (not active)
intensity = [1, 1, 1, 1] # 0 <= x <= 1
for gpio in gpios:
  GPIO.setup(gpio, GPIO.OUT)
  led = GPIO.PWM(gpio, 50)
  led.start(0)
  leds.append(led)

try:
  while True:
    # Sequence show
    # If n is number of LEDs, numbered from 0 to n - 1, then this show will
    # light all LEDs in interval [i, j] for every i, j: 0 <= i <= j < n
    for intervalLength in range(1, len(leds) + 1):
      for i in range(0, len(leds) + 1 - intervalLength):
        for dutyCycle in range(0, 101):
          for j in range(i, i + intervalLength):
            leds[j].ChangeDutyCycle(dutyCycle * intensity[j])
          sleep(0.07)
        sleep(60)
        for dutyCycle in range(100, -1, -1):
          for j in range(i, i + intervalLength):
            leds[j].ChangeDutyCycle(dutyCycle * intensity[j])
          sleep(0.07)

    # Subsets show
    # If n in number of LEDs, then this show will light all 2^n subsets of LEDs
    for n in range(1, 2**len(leds)):
       i = 0
       activate = []
       while n != 0:
         if n%2 == 1:
           activate.append(i)
         i += 1
         n /= 2
       for dutyCycle in range(0, 101):
         for index in activate:
           leds[index].ChangeDutyCycle(dutyCycle * intensity[index])
         sleep(0.07)
       sleep(60)
       for dutyCycle in range(100, -1, -1):
         for index in activate:
           leds[index].ChangeDutyCycle(dutyCycle * intensity[index])
         sleep(0.07)
   
    # If n in number of LEDs, then this show will light all 2^n subsets of LEDs
    # with 10 possibilities of light intensity
    intensity_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    for intensity in product(intensity_list, repeat=len(leds)):
      for n in range(1, 2**len(leds)):
         i = 0
         activate = []
         while n != 0:
           if n%2 == 1:
             activate.append(i)
           i += 1
           n /= 2
         for dutyCycle in range(0, 101):
           for index in activate:
             leds[index].ChangeDutyCycle(dutyCycle * intensity[index])
           sleep(0.07)
         sleep(60)
         for dutyCycle in range(100, -1, -1):
           for index in activate:
             leds[index].ChangeDutyCycle(dutyCycle * intensity[index])
           sleep(0.07)

except KeyboardInterrupt:
  pass

for led in leds:
  led.stop()
GPIO.cleanup()
