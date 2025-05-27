# Axion Elite: Quantum Physics Hardware Simulator

**Created by Pushkar (QuantumCoreDev)**

Axion Elite is a cutting-edge open-source quantum hardware education project designed to simulate key phenomena in quantum mechanics using an Arduino Uno Mini Limited Edition. It includes four interactive physical experiments inspired by H.C. Verma’s physics and real quantum optics labs — all packed inside a 25x15x5 cm box.

---

## 🔬 Key Experiments

### 1. **Quantum Random Number Generator (QRNG)**
- Uses analog noise from a photodiode to generate true quantum randomness.
- Outputs binary, decimal, and hexadecimal on OLED + Serial.

### 2. **Polarization Explorer**
- Simulates qubit orientation using linear polarizers and rotating filters.
- Visualizes Malus's Law with a photodiode sensor.

### 3. **Photoelectric Effect Simulator**
- Demonstrates Einstein’s photoelectric effect using a laser and metal plate.
- Captures energy of emitted electrons via analog readings.

### 4. **Mach–Zehnder Interferometer (MZI)**
- Mimics interference pattern behavior using dual-beam splitters and a photodiode.
- Allows optical path change and detects resulting intensity shifts.

---

## 🧰 Components Used (Top & Branded)

| Component                   | Quantity | Description                               |
|----------------------------|----------|-------------------------------------------|
| Arduino Uno Mini Limited   | 1        | Official ABX00062 Board                    |
| SSD1306 OLED Display (I2C) | 1        | 0.96” Display for output                   |
| Photodiode                 | 3        | For QRNG, MZI, and Polarization           |
| Laser Module               | 2        | Red visible lasers for Photoelectric + MZI|
| IR LED                     | 1        | For alternate optical path                |
| LDR / Light Sensor         | 1        | For additional light measurements         |
| Polarizing Film Sheet      | 2        | For polarization experiment               |
| Beamsplitter               | 2        | Realistic beam splitting setup            |
| Servo Motor (SG90)         | 2        | To rotate polarizers or mirrors           |
| Breadboard + Jumper Wires  | —        | Prototyping base                          |
| 10k Resistors              | 2–3      | For voltage dividers                      |
| Pushbutton                 | 1        | Mode selector                             |
| 3.7V Li-ion or 9V Battery  | 1        | Power supply                              |

---

## ⚡ Connection Diagram

A complete schematic (`/schematic/Axion_Schematic.png`) is provided, but here’s the summary:

| Arduino Pin | Connected To            | Purpose                      |
|-------------|--------------------------|------------------------------|
| A0          | QRNG Photodiode          | Analog noise source          |
| A1          | Photoelectric Sensor     | e⁻ energy read               |
| A2          | MZI Photodiode           | Interference detection       |
| A3          | Polarization Sensor      | Light through polarizers     |
| 2 (D2)      | Mode Selector Button     | Switches experiment          |
| 3 (D3)      | Laser (PE)               | Laser ON/OFF                 |
| 4 (D4)      | Laser (MZI)              | Laser for MZI                |
| SDA, SCL    | OLED Display (I2C)       | Display output               |

---

## 🧠 How It Works

### 🧩 Mode Switching
The device uses a button connected to digital pin 2. Each press cycles between:
- `QRNG`
- `Polarization Explorer`
- `Photoelectric Effect`
- `Mach–Zehnder Interferometer`

### 💡 OLED Output
The SSD1306 OLED displays data specific to each experiment:
- QRNG: Random bits and bytes
- Polarization: Intensity via Malus’s Law
- PE: Voltage indicating emitted electron energy
- MZI: Interference pattern values

### 📊 Serial Monitor
Full debugging/logging is available over Serial @9600 baud.

---

## 🧪 Real-World Inspiration
Inspired by:
- **HC Verma Vol I & II**: Photoelectric, Interference, and Polarization chapters
- **Google’s Quantum Playground**
- **IBM Qiskit Labs**

---

## 🔓 License
MIT License — Open to all quantum creators.

---

## 🌐 Contact & Collaboration
**Pushkar (QuantumCoreDev)**  
> Connect on GitHub

If you’re from **IITs, Google X, Microsoft Research**, or an open science org — collaborate to take Axion global!

