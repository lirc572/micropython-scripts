from machine import Pin
from neopixel import NeoPixel
import time
number = 150
pin = Pin(0, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, number)   # create NeoPixel driver on GPIO0 for 8 pixels
reset = False
r, g, b = 0, 0, 0
while True:
    for i in range(number):
        n = i if reset else 149-i
        if reset:
            r, g, b = 0, 0, 0
        else:
            r, g, b = time.ticks_cpu() % 255, time.ticks_cpu() % 255, time.ticks_cpu() % 255;
        np[n] = (r, g, b)
        np.write()
        print(n, np[n])
        time.sleep_ms(20)
    reset = not reset