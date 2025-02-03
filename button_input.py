from gpiozero import Button
from time import sleep

# Define buttons using Broadcom (BCM) numbering
start_button = Button(18, pull_up=True)  # GPIO18 corresponds to physical pin 12
stop_button = Button(23, pull_up=True)   # GPIO23 corresponds to physical pin 16

end = False

while not end:
    if start_button.is_pressed:
        print('Start was pressed')
        sleep(0.5)
    if stop_button.is_pressed:
        print('Stop was pressed')
        sleep(0.5)
    if start_button.is_pressed and stop_button.is_pressed:
        print('Make up your mind!')
        end = True
