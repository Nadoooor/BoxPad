# BoxPad
---------------------

<p align="center">
  <img src="Photos/Rendered.PNG" alt="Centered Image" width="600">
</p>

-------------------

## Description:
A macropad in a cheese box. This is a macropad made from scratch with MX switches, and it can be totaly made by DIYing (Recycling, and handwiring), or by just printing the case and the PCB.

## Why making this?
Well, I have many hardware components and I want to make something with them, but 3D printing and PCB printing in Egypt costs so much, so gonna DIY it from scratch.

> [!NOTE]
> AI helped a lil with the firmware DOCS because KMK & QMK are kinda outdated

## Features:
- MX switchs in a 2x4 Metrix.
- OLED 0.96' Screen.
- Rotary Encoder.
- NEO sticks.

## Photos & Demo:

### Schematic:
![alt text](Photos/Schem.png)

### PCB:
![alt text](Photos/PCB.png)

### 3D PCB:
![alt text](Photos/3Dpcb.png)

### 3D Assembly:
![3D](Photos/Rendered.png)

> [!NOTE]
> Here you are the [Fusion Assembly](https://a360.co/4h1u5xi)

### Demo Video:
<video controls src="Demo.mp4" title="Demo Video of BoxPad"></video>

## How to Build (Using Printed Parts):

1. Print all your parts.
2. Put the MX Switches in their places on the cover.
3. Solder the screen and the Rotary Encoder.
4. Place the PCB under the switches and Solder them.
5. Solder the XIAO on the board, using its pin header so you can control its height.
6. Solder the JST connector of the NEOsticks 
7. Connect the NEOsticks, and put them inside the case corners using hot glue.
8. Download CircuitPython, and install it into the XIAO RP2040.
9. Copy What's inside the [Firmware Folder](Firmware), and paste it inside the CIRCUITPY Drive.
10. Replug the MCU and it will run automaticly.

## How to Build (DIYing):

1. Find any Box to recycle. (Like a cheese box).
2. Cut the exact mesurements of the SWs, rotary encoder, and OLED screen holes on the cover of the box.
3. Put the SWs, and the rotary encoder on the cover of the box.
4. Hand wire and solder the Diodes and the ROWs and COLs from the back, also the Rotary encoder and the OLED.
5. Solder a 4 NEOsticks chain, and using hot glue put them inside the box.
6. Connect everything to the XIAO PinHeader (or use a small breadboard).
7. Connect the XIAO to the PC/Laptop.
8. Use the same steps as in step (8) in (How to bulid using printed parts.)

---------------
# Made with ❤️, By @Nadoooor
