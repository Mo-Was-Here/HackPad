{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import board\
from kmk.kmk_keyboard import KMKKeyboard\
from kmk.keys import KC\
from kmk.extensions.media_keys import MediaKeys\
from kmk.modules.encoder import EncoderHandler\
from kmk.modules.layers import Layers\
from kmk.extensions.peg_rgb import RGB\
\
# 1. Initialize the keyboard core framework\
keyboard = KMKKeyboard()\
keyboard.extensions.append(MediaKeys())\
keyboard.modules.append(Layers())\
\
# 2. Map your 3 Keyswitches (Pin 11=D10, Pin 10=D9, Pin 9=D8)\
keyboard.pins = [board.D10, board.D9, board.D8]\
\
# 3. Setup the Rotary Encoder (Pin 1=D0, Pin 2=D1, Switch Pin 3=D2)\
encoder_handler = EncoderHandler()\
keyboard.modules.append(encoder_handler)\
encoder_handler.pins = ((board.D0, board.D1, board.D2, False),)\
\
# 4. Setup your 2 RGB Backlights (Data Pin 7=D6, Total LEDs=2)\
rgb = RGB(pixel_pin=board.D6, num_pixels=2)\
keyboard.extensions.append(rgb)\
\
# 5. Define what your keys and knob actually do!\
# Mapped to Copy, Paste, and a custom system Mute macro\
keyboard.keymap = [\
    [KC.LCMD(KC.C), KC.LCMD(KC.V), KC.MUTE]\
]\
\
# The Rotary Encoder Rotation: Turn left for Volume Down, right for Volume Up\
encoder_handler.map = [\
    ((KC.VOLD, KC.VOLU),)\
]\
\
if __name__ == '__main__':\
    keyboard.go()\
}