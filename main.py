from machine import Pin
import time

pin17=Pin(17,Pin.OUT)


while True:
  pin17.value(0)
  time.sleep(100 / 1000);
  pin17.value(1)
  time.sleep(100 / 1000);