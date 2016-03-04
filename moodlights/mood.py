#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep
from itertools import product

GPIO.setmode(GPIO.BCM)

LED_GPIO = [26, 19, 13, 6] # blue, green, yellow, red
leds = []
duty_cycles = [0, 0, 0, 0]

def fade_to_intensity(led_indexes, intensity, sleep_time):
  global duty_cycles
  step = [1 for x in range(0, len(led_indexes))]
  for i, val in enumerate(led_indexes):
    if duty_cycles[val] > intensity[i]:
      step[i] *= -1
  
  cnt = 0
  while cnt != len(led_indexes):
    cnt = 0
    for i, val in enumerate(led_indexes):
      if duty_cycles[val] == intensity[i]:
        cnt += 1
      else:
        duty_cycles[val] += step[i]
        leds[val].ChangeDutyCycle(duty_cycles[val])
    sleep(sleep_time) 

def subset_show():
  global duty_cycles
  intensity_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
  for subset in range(1, 2**len(leds)):
    index = 0
    led_indexes = []
    while subset != 0:
      if subset%2 == 1:
        led_indexes.append(index)
      index += 1
      subset /= 2 
    
    for intensity in product(intensity_values, repeat=len(led_indexes)):
      fade_to_intensity(led_indexes, [x * 100 for x in intensity], 0.07)
      sleep(0.07) 
    
    fade_to_intensity(led_indexes, [0 for x in range(0, len(led_indexes))], 0.07)

def main():
  for gpio in LED_GPIO:
    GPIO.setup(gpio, GPIO.OUT)
    led = GPIO.PWM(gpio, 50)
    led.start(0) # start with 0 duty cycle
    leds.append(led)
  
  try:
    while True:
      subset_show()
  except KeyboardInterrupt:
    pass

  for led in leds:
    led.stop() 
  GPIO.cleanup()

if __name__ == "__main__":
  main()
