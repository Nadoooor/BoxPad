print("Starting")

import board
import time
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
encoder_handler = EncoderHandler()
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rgb import RGB
from kmk.extensions.rgb import AnimationModes
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306  
from kmk.modules.layers import Layers


keyboard = KMKKeyboard()
layers = Layers()

keyboard.modules = [encoder_handler, layers]

mediakeys = MediaKeys()
keyboard.extensions.append(mediakeys)

# keyboard cols and rows
keyboard.col_pins = (board.D3, board.D2, board.D1, board.D0)
keyboard.row_pins = (board.D7, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# RGB
rgb = RGB(pixel_pin=board.D6,
        num_pixels=16,
        val_limit=100, 
        hue_default=0,
        sat_default=100,
        rgb_order=(1, 0, 2),  # GRB WS2812
        animation_mode=AnimationModes.STATIC,
        )
keyboard.extensions.append(rgb)

#Display
i2c_bus = busio.I2C(board.SCL, board.SDA)

driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

display = Display(
    
    display=driver,
    
    width=128, 
    height=64, 
)

display.entries = [
    TextEntry(text="This Macropad", x=0, y=0),
    TextEntry(text="Was made with ♥ By", x=0, y=12),
    TextEntry(text="NADOOOOR", x=0, y=24),
]
keyboard.extensions.append(display)

scanfunc = keyboard.after_matrix_scan
lastlayer = 0

def layers_handling(*args, **kwargs):
    global lastlayer
    scanfunc()
    curlayer = keyboard.active_layers[0]    
    if lastlayer != curlayer:
        lastlayer = curlayer
        display.entries = []   

        if curlayer == 0:
            display.entries.append(TextEntry(text="Media Layer!!\n", x=0, y=0))
            display.entries.append(TextEntry(text="Encoder: Volume\n", x=0, y=12))
            rgb.set_rgb_fill((0, 255, 0))
            

        elif curlayer == 1:
            display.entries.append(TextEntry(text="Work Layer!!\n", x=0, y=0))
            display.entries.append(TextEntry(text="Encoder: Scroll\n", x=0, y=12))
            rgb.set_rgb_fill((255, 0, 0))
            
        elif curlayer == 2:
            display.entries.append(TextEntry(text="Browsing Layer!!\n", x=0, y=0))
            display.entries.append(TextEntry(text="Encoder: Tap_switching\n", x=0, y=12))
            rgb.set_rgb_fill((0, 0, 255))
            
    
keyboard.after_matrix_scan = layers_handling
# Encoder

encoder_handler.pins = (
    (board.MOSI, board.MISO, None), 
    )



# mappings
encoder_handler.map = [ 
    (( KC.VOLU, KC.VOLD),),
    (( KC.PGUP, KC.PGDN),),
    (( KC.LCTRL(KC.TAB), KC.LCTRL(KC.LSHIFT(KC.TAB))),),
    ] 

keyboard.keymap = [
    # Layer 1 (Media)

    [KC.MPLY, KC.MUTE, KC.MNXT, KC.TO(1),
     KC.MPRV, KC.ENT, KC.SPC, KC.ESC],

     # Layer 2 (Work)
    [KC.LCTRL(KC.C), KC.LCTRL(KC.Y), KC.HOME, KC.TO(2),
     KC.LCTRL(KC.V), KC.LCTRL(KC.Z), KC.END, KC.DEL],

     # Layer 3 (BROWSING)
     [KC.LCTRL(KC.T), KC.MUTE, KC.F5, KC.TO(0),
     KC.LALT(KC.LEFT), KC.LALT(KC.RIGHT), KC.LCTRL(KC.MINUS), KC.LCTRL(KC.EQUAL)]
]

if __name__ == '__main__':
    keyboard.go()

