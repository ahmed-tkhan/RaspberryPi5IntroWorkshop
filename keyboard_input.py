from gpiozero import LED
from time import sleep

led = LED(17)  # GPIO17 corresponds to physical pin 11

# Get user input for the number of blinks
blink_num = int(input('How many times do you want to blink? '))

# Blink the LED as many times as specified by the user
for _ in range(blink_num):
    led.on()   # Turn the LED on
    sleep(1)   # Wait for 1 second
    led.off()  # Turn the LED off
    sleep(1)   # Wait for 1 second
