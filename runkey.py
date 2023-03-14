# ref: https://www.instructables.com/DIY-Macro-Keyboard-Using-a-Raspberry-PI-Pico/
# circuit python firmware: https://circuitpython.org/board/raspberry_pi_pico/
# adafruit_hid lib: https://github.com/adafruit/Adafruit_CircuitPython_HID/releases
# Pico diagram: https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html

import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

run_pin = board.GP19

run = digitalio.DigitalInOut(run_pin)
run.direction = digitalio.Direction.INPUT
run.pull = digitalio.Pull.DOWN

print('Start...')
while True:
    if run.value:  
        print("Run Code!")
        keyboard.press(Keycode.F5)
        time.sleep(0.15)
        keyboard.release(Keycode.F5)
    time.sleep(0.1)