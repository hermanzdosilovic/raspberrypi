#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep
from itertools import product

GPIO.setmode(GPIO.BCM)

LED_GPIO = [26, 19, 13, 6] # blue, green, yellow, red
leds = []

def fadein(led_indexes, intensity, sleep_time):
  for dc in range(0, 101):
    for i, val in enumerate(led_indexes):
      leds[val].ChangeDutyCycle(dc * intensity[i])
    sleep(sleep_time) 

def fadeout(led_indexes, intensity, sleep_time):
  for dc in range(100, -1 , -1):
    for i, val in enumerate(led_indexes):
      leds[val].ChangeDutyCycle(dc * intensity[i])
    sleep(sleep_time) 

def subset_show():
  intensity_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
  for subset in range(1, 2**len(leds)):
    index = 0
    led_indexes = []
    while subset != 0:
      if subset%2 == 1:
        led_indexes.append(index)
      index += 1
      subset /= 2 
    
    fadein(led_indexes, [1 for x in range(0, len(led_indexes))], 0.07) 
    fadeout(led_indexes, [1 for x in range(0, len(led_indexes))], 0.07) 

def main():
  for gpio in LED_GPIO:
    GPIO.setup(gpio, GPIO.OUT)
    led = GPIO.PWM(gpio, 50)
    led.start(0) # start with 0 duty cycle
    leds.append(led)
  
  try:
    while True:
      subset_show()
  except:
    pass

  for led in leds:
    led.stop() 
  GPIO.cleanup()

if __name__ == "__main__":
  main()
