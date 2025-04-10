# Axion – Optical Quantum Random Number Generator

![Axion Logo](https://img.shields.io/badge/Quantum-Randomness-green)

> Built by Pushkar (14 y/o innovator, aka [QuantumCoreDev](https://github.com/QuantumCoreDev))

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
- SDA (OLED + ADS1115) → GPIO 21
- SCL (OLED + ADS1115) → GPIO 22
- Photodiodes → A0 and A1 on ADS1115
- OLED VCC → 3.3V
- Laser → Boosted 5V from MT3608

## 🚀 How to Use
1. Flash MicroPython to ESP32
2. Upload `main.py` and `web/` using Thonny/uPyCraft
3. Update SSID & PASSWORD in code
4. Connect and access via browser at IP address

## 📄 License
MIT – Open-source and open for innovation!