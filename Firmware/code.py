print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
encoder_handler = EncoderHandler()

keyboard.modules = [layers, holdtap, encoder_handler]

keyboard = KMKKeyboard()


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