import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import board
import digitalio
import time

time.sleep(1.5)

btn1_pin = board.GP0
btn2_pin = board.GP1
btn3_pin = board.GP2
btn4_pin = board.GP3
btn5_pin = board.GP4
btn6_pin = board.GP5

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN

encoder_click = digitalio.DigitalInOut(encoder_click_pin)
encoder_click.direction = digitalio.Direction.INPUT
encoder_click.pull = digitalio.Pull.DOWN

keyboard = Keyboard(usb_hid.devices)
consumer_control = ConsumerControl(usb_hid.devices)

while True:

    # Status LED
    led.value = True

    if btn1.value:
        consumer_control.send(ConsumerControlCode.MUTE)
        time.sleep(0.1)
    if btn2.value:
        consumer_control.send(ConsumerControlCode.VOLUME_INCREMENT)
        time.sleep(0.1)
    if btn3.value:
        consumer_control.send(ConsumerControlCode.VOLUME_DECREMENT)
        time.sleep(0.1)
    if btn4.value:
        consumer_control.send(ConsumerControlCode.PLAY_PAUSE)
        time.sleep(0.1)
    if btn5.value:
        consumer_control.send(ConsumerControlCode.SCAN_NEXT_TRACK)
        time.sleep(0.1)
    if btn6.value:
        consumer_control.send(ConsumerControlCode.MUTE)
        time.sleep(0.1)
    time.sleep(0.1)
