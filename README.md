# HackPad
# 🚀 My Custom 3-Key Hackpad

A custom 3-key mechanical macro keypad featuring an integrated rotary encoder dial and individually addressable RGB backlight LEDs. The entire hardware framework is driven by a Seeed Studio XIAO RP2040 microcontroller and runs on the Python-based KMK keyboard firmware framework.

---

## 📸 Project Previews

### 📐 1. Overall Assembled Enclosure
*Replace this line with your Tinkercad workspace 3D canvas layout view or export screenshot.*

### ⚡ 2. Circuit Schematic Layout
*Replace this line with a screenshot of your clean, 0-error KiCad schematic sheet.*

### 🟢 3. Physical PCB Traces (2D View)
*Replace this line with a screenshot of your red F.Cu and blue B.Cu copper routed tracks.*

### 🛠️ 4. Assembled PCB Model (3D View)
*Replace this line with a screenshot of your finished board generated in the KiCad 3D Viewer (Option + 3).*

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
