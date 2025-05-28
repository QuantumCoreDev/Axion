# 🔧 Setup Guide for Axion 

This guide explains how to assemble, wire, and upload code to the Arduino UNO Mini Limited Edition for the Axion project.

---

## 📦 Components Needed

### 🧠 Core Microcontroller
- Arduino UNO Mini Limited Edition (ABX00062)

### 🔍 Sensors & Detectors
- High-sensitivity Photodiode (x3)
- Analog Light Sensor (backup or visualization)

### 🔦 Light Sources
- 650nm Red Laser Module (x2)

### ⚙️ Actuators
- SG90 Micro Servo Motor (x2)

### 🧲 Optical Components
- Polarizing Sheets (x2)
- Beam Splitter (x1)
- Plane Mirrors (x2)
- Metal Foil Target (for Photoelectric Effect)

### 📟 Display
- 128x64 I2C OLED Display (SSD1306)

### 🔘 Input
- Tactile Push Button (x1)

### 🔗 Misc
- Breadboard & Jumper Wires
- Resistors (10kΩ, 220Ω as needed)
- Power Source (USB or 9V Battery with Jack)

---

## 🧷 Wiring Instructions

### OLED Display (I2C)
- **VCC** → 5V
- **GND** → GND
- **SCL** → A5
- **SDA** → A4

### Push Button
- One side to **pin 2** (with pull-down 10kΩ resistor)
- Other side to **+5V**

### Servo Motors
- Servo 1 (Polarization): **Signal → pin 5**
- Servo 2 (MZI): **Signal → pin 6**
- VCC → 5V (with capacitor decoupling)
- GND → GND

### Photodiodes
- QRNG → **A0**
- Polarization Explorer → **A1**
- Photoelectric Effect → **A2**
- MZI → **A3**

### Lasers
- Powered from regulated 5V (shared rail) with switch

---

## ⚙️ Uploading the Code

1. Install **Arduino IDE** (v1.8.x or 2.x)
2. Go to **Tools > Board > Arduino AVR Boards > Arduino Uno**
3. Select correct COM port under **Tools > Port**
4. Paste code from `Axion_Quantum_Experiments.ino`
5. Click ✅ **Verify** and ⬆️ **Upload**

---

## 🧪 Running Experiments

- Power the system using USB or 9V source.
- Use the button to cycle through:
  - `Quantum RNG`
  - `Polarization Explorer`
  - `Photoelectric Effect`
  - `Mach-Zehnder Interferometer`
- Live results are shown on OLED.
- For graphs and debugging, open the **Serial Monitor**.

---

## 📏 Physical Assembly Notes

- Mount components on a 25x15x5cm foam-core base or cardboard box.
- Use black masking tape to isolate optical paths.
- Elevate mirrors and lasers to same height (~2–3cm)
- Secure optics using glue tack or foam mounts

--- 

> With proper care and calibration, Axion becomes a functional hands-on physics lab. Ideal for presentations, demo days, or quantum learning fairs.
