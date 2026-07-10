print("Starting")

import board
import busio
import displayio
import terminalio
import adafruit_displayio_ssd1306

from adafruit_display_text import label
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB, AnimationModes
encoder_handler = EncoderHandler()
from kmk.kmk_keyboard import KMKKeyboard

keyboard.modules = [layers, holdtap, encoder_handler]

i2c = busio.I2C(scl=board.SCL, sda=board.SDA)

display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306_I2C(display_bus, width=128, height=64)

text_area = label.Label(
    terminalio.FONT, 
    text="Made with LOVE, by @Nadoooor", 
    color=0xFFFFFF, 
    x=10, 
    y=25
)

splash = displayio.Group()
splash.append(text_area)
display.show(splash)


keyboard = KMKKeyboard()

rgb = RGB(
    val_default=10,
    val_limit=100,  # out of 255
    pixel_pin=board.D6,
    num_pixels=32,
    refresh_rate=30,
    animation_speed=3,
    animation_mode=AnimationModes.STATIC,
)
keyboard.extensions.append(rgb)

encoder_handler.pins = (
    (board.D10, board.D9, NONE)
    )
keyboard.col_pins = (board.D3, board.D2, board.D1, board.D0)
keyboard.row_pins = (board.D7,board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.F5, KC.F11, KC.PSCREEN, KC.RGUI],
    [KC.F6, KC.F1, KC.ESC, KC.TRNS]
]
encoder_handler.map = [ ((KC.VOLU, KC.VOLD, KC.NONE))



if __name__ == '__main__':
    keyboard.go()