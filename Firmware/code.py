print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB, AnimationModes
encoder_handler = EncoderHandler()

keyboard.modules = [layers, holdtap, encoder_handler]

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