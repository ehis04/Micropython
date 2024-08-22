# Toggle led connected to Pin 15
from machine import Pin
import time

led = Pin(15, Pin.OUT)

for _ in range(5):
    led.toggle()
    time.sleep(1)
    
