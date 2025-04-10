# Axion – Optical Quantum Random Number Generator

Built by Pushkar (14 y/o innovator, aka [QuantumCoreDev](https://github.com/QuantumCoreDev))

Axion is a microcontroller-powered QRNG that uses light, optics, and photon behavior to produce true quantum randomness.

## ✨ Features
- Photon-based entropy source
- ESP32 + ADS1115 + OLED + Laser + Beam Splitter
- OLED screen shows live entropy
- Web interface updates every 2s
- Debiased bits for better randomness

## 🛠 Hardware Used
- ESP32 Dev Module (NodeMCU)
- ADS1115 ADC Module
- BPW-Z Photodiodes × 2
- HW-493 Laser Diode
- 50/50 Cube Beam Splitter (15x15mm)
- MT3608 Step-up Converter
- OLED 0.96" I2C Display
- Resistors and capacitors

## 🔌 Wiring Guide
### ✅ 1. ESP32 I2C Connections (Shared by OLED & ADS1115)

| ESP32 Pin | Connects To           | Description       |
|-----------|------------------------|-------------------|
| GPIO 21   | SDA (OLED + ADS1115)   | I2C Data Line     |
| GPIO 22   | SCL (OLED + ADS1115)   | I2C Clock Line    |
| 3.3V      | OLED VCC               | OLED Power        |
| GND       | OLED GND               | OLED Ground       |
| 3.3V      | ADS1115 VCC            | ADS Power         |
| GND       | ADS1115 GND            | ADS Ground        |

> ✅ OLED & ADS1115 **share the I2C bus**, and that’s totally fine!

---

### ✅ 2. Photodiodes → ADS1115 Analog Inputs

| Photodiode     | Connects To    |
|----------------|----------------|
| PD-A Signal    | A0 (ADS1115)   |
| PD-B Signal    | A1 (ADS1115)   |
| PD GND (Both)  | GND (ESP32)    |
| Pull-down Resistors | 10k (Optional on A0/A1) |

> 🧪 **BPW-Z photodiodes** output analog voltage based on light.

---

### ✅ 3. Laser Diode (HW-493)

| Laser Pin | Connects To                 |
|-----------|-----------------------------|
| + (VCC)   | OUT+ of MT3608 Boost (5V)   |
| – (GND)   | GND (MT3608 or ESP32)       |

> MT3608 boosts 3.3V → **5V** to power the laser.

---

### ✅ 4. MT3608 Step-Up Module

| MT3608 Pin | Connects To     |
|------------|-----------------|
| IN+        | 3.3V from ESP32 |
| IN–        | GND of ESP32    |
| OUT+       | Laser VCC (+5V) |
| OUT–       | Laser GND       |

> 🔧 Adjust the potentiometer clockwise to get a **5V output** (check with multimeter).

---

### ✅ 5. Powering the ESP32

- Use a **USB cable** to power the ESP32 (recommended)
- You can also use a **Li-ion battery + boost converter** for portable setups
- ESP32 provides both **3.3V and GND** rails for components


## 🚀 How to Use
1. Flash MicroPython to ESP32
2. Upload `main.py` and `web/` using Thonny/uPyCraft
3. Update SSID & PASSWORD in code
4. Connect and access via browser at IP address

## 📄 License
MIT – Open-source and open for innovation!
