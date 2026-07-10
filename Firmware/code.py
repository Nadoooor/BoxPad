print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D3, board.D2, board.D1, board.D0)
keyboard.row_pins = (board.D7,board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.F5, KC.F11, KC.PSCREEN, KC.RGUI],
    [KC.F6, KC.F1, KC.ESC, KC.TRNS]
]

if __name__ == '__main__':
    keyboard.go()