import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Pin definitions
button_pin_a = digitalio.DigitalInOut(board.A0)
button_pin_a.direction = digitalio.Direction.INPUT
button_pin_a.pull = digitalio.Pull.UP

button_pin_s = digitalio.DigitalInOut(board.A1)
button_pin_s.direction = digitalio.Direction.INPUT
button_pin_s.pull = digitalio.Pull.UP

button_pin_d = digitalio.DigitalInOut(board.A2)
button_pin_d.direction = digitalio.Direction.INPUT
button_pin_d.pull = digitalio.Pull.UP

button_pin_w = digitalio.DigitalInOut(board.A3)
button_pin_w.direction = digitalio.Direction.INPUT
button_pin_w.pull = digitalio.Pull.UP

button_pin_o = digitalio.DigitalInOut(board.D13)
button_pin_o.direction = digitalio.Direction.INPUT
button_pin_o.pull = digitalio.Pull.UP

button_pin_i = digitalio.DigitalInOut(board.D12)
button_pin_i.direction = digitalio.Direction.INPUT
button_pin_i.pull = digitalio.Pull.UP

button_pin_u = digitalio.DigitalInOut(board.D11)
button_pin_u.direction = digitalio.Direction.INPUT
button_pin_u.pull = digitalio.Pull.UP

button_pin_j = digitalio.DigitalInOut(board.D10)
button_pin_j.direction = digitalio.Direction.INPUT
button_pin_j.pull = digitalio.Pull.UP

button_pin_k = digitalio.DigitalInOut(board.D9)
button_pin_k.direction = digitalio.Direction.INPUT
button_pin_k.pull = digitalio.Pull.UP

button_pin_l = digitalio.DigitalInOut(board.D6)
button_pin_l.direction = digitalio.Direction.INPUT
button_pin_l.pull = digitalio.Pull.UP

# Create a Keyboard object
kbd = Keyboard(usb_hid.devices)

# Function to send the key press
def send_key(key):
    kbd.press(key)

# Function to release the key
def release_key(key):
    kbd.release(key)

# Main loop
keys_pressed = set()  # Track the currently pressed keys
while True:
    # Check if the "A" button is pressed (the pin goes LOW when the button is pressed)
    if not button_pin_a.value:
        if Keycode.A not in keys_pressed:
            send_key(Keycode.A)
            keys_pressed.add(Keycode.A)
    else:
        if Keycode.A in keys_pressed:
            release_key(Keycode.A)
            keys_pressed.remove(Keycode.A)

    # Check if the "S" button is pressed (the pin goes LOW when the button is pressed)
    if not button_pin_s.value:
        if Keycode.S not in keys_pressed:
            send_key(Keycode.S)
            keys_pressed.add(Keycode.S)
    else:
        if Keycode.S in keys_pressed:
            release_key(Keycode.S)
            keys_pressed.remove(Keycode.S)

    # Check if the "D" button is pressed (the pin goes LOW when the button is pressed)
    if not button_pin_d.value:
        if Keycode.D not in keys_pressed:
            send_key(Keycode.D)
            keys_pressed.add(Keycode.D)
    else:
        if Keycode.D in keys_pressed:
            release_key(Keycode.D)
            keys_pressed.remove(Keycode.D)

    # Check if the "W" button is pressed (the pin goes LOW when the button is pressed)
    if not button_pin_w.value:
        if Keycode.W not in keys_pressed:
            send_key(Keycode.W)
            keys_pressed.add(Keycode.W)
    else:
        if Keycode.W in keys_pressed:
            release_key(Keycode.W)
            keys_pressed.remove(Keycode.W)

    # Check if the "O" button is pressed (the pin goes LOW when the button is pressed)
    if not button_pin_o.value:
        if Keycode.O not in keys_pressed:
            send_key(Keycode.O)
            keys_pressed.add(Keycode.O)
    else:
        if Keycode.O in keys_pressed:
            release_key(Keycode.O)
            keys_pressed.remove(Keycode.O)

    # Check if the "I" button is pressed (the pin goes LOW when the button is pressed)
    if not button_pin_i.value:
        if Keycode.I not in keys_pressed:
            send_key(Keycode.I)
            keys_pressed.add(Keycode.I)
    else:
        if Keycode.I in keys_pressed:
            release_key(Keycode.I)
            keys_pressed.remove(Keycode.I)

    # Check if the "U" button is pressed (the pin goes LOW when the button is pressed)
    if not button_pin_u.value:
        if Keycode.U not in keys_pressed:
            send_key(Keycode.U)
            keys_pressed.add(Keycode.U)
    else:
        if Keycode.U in keys_pressed:
            release_key(Keycode.U)
            keys_pressed.remove(Keycode.U)

    # Check if the "J" button is pressed (the pin goes LOW when the button is pressed)
    if not button_pin_j.value:
        if Keycode.J not in keys_pressed:
            send_key(Keycode.J)
            keys_pressed.add(Keycode.J)
    else:
        if Keycode.J in keys_pressed:
            release_key(Keycode.J)
            keys_pressed.remove(Keycode.J)

    # Check if the "K" button is pressed (the pin goes LOW when the button is pressed)
    if not button_pin_k.value:
        if Keycode.K not in keys_pressed:
            send_key(Keycode.K)
            keys_pressed.add(Keycode.K)
    else:
        if Keycode.K in keys_pressed:
            release_key(Keycode.K)
            keys_pressed.remove(Keycode.K)

    # Check if the "L" button is pressed (the pin goes LOW when the button is pressed)
    if not button_pin_l.value:
        if Keycode.L not in keys_pressed:
            send_key(Keycode.L)
            keys_pressed.add(Keycode.L)
    else:
        if Keycode.L in keys_pressed:
            release_key(Keycode.L)
            keys_pressed.remove(Keycode.L)

    # Add a small delay to avoid excessive key presses (adjust as needed)
    time.sleep(0.025)
