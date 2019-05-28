from pad4pi import rpi_gpio
import time
import os
import sys

# Setup Keypad
KEYPAD = [
        ["record","process","origen","gegant"],
        ["frere","imperial","6","exit"],
        ["7","8","9","C"],
        ["*","0","#","D"]
]

# same as calling: factory.create_4_by_4_keypad, still we put here fyi:
ROW_PINS = [4, 14, 15, 17] # BCM numbering
COL_PINS = [18, 27, 22, 23] # BCM numbering

factory = rpi_gpio.KeypadFactory()

# Try factory.create_4_by_3_keypad
# and factory.create_4_by_4_keypad for reasonable defaults
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

#keypad.cleanup()

def printKey(key):
    print(key)
    if key == "record":
        print("Estas grabando un audio")
        os.system("arecord -d 5 --device=plughw:1,0 --format S16_LE --rate 44100 -c1 test.wav")
        print("Grabación finalizada")
    elif key == "process":
        os.system("python3 scripts/note_detector.py test.wav")
    elif key == "origen":
        print("ejecutando servosOrigen.py")
        os.system("python3 scripts/servosOrigen.py")
    elif key == "gegant":
        print("Tocando el Gegant del Pi")
        os.system("python3 scripts/codiTocar.py 1")
    elif key == "frere":
        print("Tocando Frere Jacques")
        os.system("python3 scripts/codiTocar.py 2")
    elif key == "imperial":
        print("Tocando Imperial March")
        os.system("python3 scripts/codiTocar.py 3")
    elif key == "exit":
        keypad.cleanup()
        sys.exit()

# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(printKey)

try:
  while(True):
    time.sleep(0.2)
except:
 keypad.cleanup()
