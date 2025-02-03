from gpiozero import LED
from time import sleep

led = LED(17)  # GPIO17 corresponds to physical pin 11

while True:
    led.on()    # Turn the LED on
    sleep(1)    # Wait for 1 second
    led.off()   # Turn the LED off
    sleep(1)    # Wait for 1 second
