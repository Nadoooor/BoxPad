print("Starting")

import board
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


keyboard = KMKKeyboard()

keyboard.modules = [encoder_handler]
# Regular GPIO Encoder

keyboard.extensions.append(MediaKeys())


keyboard.col_pins = (board.D3, board.D2, board.D1, board.D0)
keyboard.row_pins = (board.D7, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

rgb = RGB(pixel_pin=board.D6,
        num_pixels=16,
        val_limit=100, 
        hue_default=0,
        sat_default=100,
        rgb_order=(1, 0, 2),  # GRB WS2812
        val_default=100,
        hue_step=5,
        sat_step=5,
        val_step=5,
        animation_speed=1,
        breathe_center=1,  # 1.0-2.7
        knight_effect_length=3,
        animation_mode=AnimationModes.SWIRL,
        reverse_animation=False,
        refresh_rate=60,
        )
keyboard.extensions.append(rgb)


i2c_bus = busio.I2C(board.SCL, board.SDA)

driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

display = Display(
    # Mandatory:
    display=driver,
    # Optional:
    width=128, # screen size
    height=64, # screen size
    flip = False, # flips your display content
    flip_left = False, # flips your display content on left side split
    flip_right = False, # flips your display content on right side split
    brightness=0.8, # initial screen brightness level
    brightness_step=0.1, # used for brightness increase/decrease keycodes
    dim_time=20, # time in seconds to reduce screen brightness
    dim_target=0.1, # set level for brightness decrease
    off_time=60, # time in seconds to turn off screen
    powersave_dim_time=10, # time in seconds to reduce screen brightness
    powersave_dim_target=0.1, # set level for brightness decrease
    powersave_off_time=30, # time in seconds to turn off screen
)

display.entries = [
    TextEntry(text="This Macropad", x=0, y=0),
    TextEntry(text="Was made with ♥ By", x=0, y=12),
    TextEntry(text="NADOOOOR", x=0, y=24),
]
keyboard.extensions.append(display)



encoder_handler.pins = (
    
    (board.MOSI, board.MISO, None), # encoder #1 
    )

encoder_handler.map = [ (
    
    ( KC.RGB_HUI, KC.RGB_HUD, KC.MUTE),
                         
                         ),] 





keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D,
     KC.E, KC.F, KC.G, KC.H]
]

if __name__ == '__main__':
    keyboard.go()

