# 🚀 My Custom 3-Key Hackpad

> ⚠️ **Development Note:** The current 3D enclosure base file (`Top.STL`) is an initial layout draft to fulfill the folder architecture requirements. It is not currently matched to the exact final physical dimensions of the routed PCB and will be updated with precise mechanical alignments before final hardware fabrication.


A custom 3-key mechanical macro keypad featuring an integrated rotary encoder dial and individually addressable RGB backlight LEDs. The entire hardware framework is driven by a Seeed Studio XIAO RP2040 microcontroller and runs on the Python-based KMK keyboard firmware framework.

---

## 📐 Project Structure

This repository contains all source and manufacturing files required to build this project, organized according to Hack Club's shipping guidelines:
* `/CAD` - Contains the structural 3D design file (Top.STL) for the switch plate enclosure.
* `/PCB` - Contains the editable KiCad project, schematic, and board layout files.
* `/firmware` - Contains the core KMK configuration script (main.py).
* `/production` - Contains the manufacturing-ready gerbers.zip bundle and configuration assets.

---

## 📋 Bill of Materials (BOM)


| Component | Description | Qty | Part Source Link |
| :--- | :--- | :---: | :--- |
| **MCU** | Seeed Studio XIAO RP2040 Module | 1 | [Seeed Studio Official](https://seeedstudio.com) |
| **Switches** | Cherry MX Mechanical Keyswitches | 3 | [DigiKey Catalog](https://digikey.com) |
| **Encoder** | EC11 Rotary Encoder Dial with Built-in Switch | 1 | [Adafruit Supply](https://adafruit.com) |
| **LEDs** | SK6812MINI-E Individual Addressable RGB Components | 2 | [JLCPCB Parts Library](https://jlcpcb.com) |
| **Enclosure** | 1.5mm Custom 3D-Printed Switch Plate Base Shell | 1 | *Custom Manufactured STL File* |

---

## 🛠️ Pinout Mapping Reference

*   **SW1 (Key 1)** $\rightarrow$ GPIO Pin 11 (`board.D10`)
*   **SW2 (Key 2)** $\rightarrow$ GPIO Pin 10 (`board.D9`)
*   **SW3 (Key 3)** $\rightarrow$ GPIO Pin 9 (`board.D8`)
*   **Rotary Encoder Pins** $\rightarrow$ A: Pin 1 (`board.D0`) / B: Pin 2 (`board.D1`) / Switch: Pin 3 (`board.D2`)
*   **NeoPixel Data Bus** $\rightarrow$ Pin 7 (`board.D6`)
*   **Common Rails** $\rightarrow$ Positive: `+3V3` / Negative Return Path: `GND`

---

## 💻 Firmware Setup Instructions
This board runs CircuitPython with the KMK framework library. To deploy:
1. Flash the Seeed Studio XIAO with the latest CircuitPython .UF2 payload.
2. Copy the `kmk` firmware directory onto the root directory of the microcontroller storage volume.
3. Move the provided `main.py` configuration script onto the board to instantly map keybinds and lighting profiles.
