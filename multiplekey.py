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
        keyboard.press(Keycode.LEFT_SHIFT)
        keyboard.press(Keycode.LEFT_CONTROL)
        keyboard.press(Keycode.I)
        time.sleep(0.15)
        keyboard.release(Keycode.LEFT_SHIFT)
        keyboard.release(Keycode.LEFT_CONTROL)
        keyboard.release(Keycode.I)
    time.sleep(0.1)