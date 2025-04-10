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
🧠 Axion QRNG – (Wiring Guide)
✅ 1. ESP32 I2C (Shared by OLED & ADS1115)
ESP32 Pin	Connects To	Used By
GPIO 21	SDA (OLED + ADS1115)	I2C Data Line
GPIO 22	SCL (OLED + ADS1115)	I2C Clock
3.3V	OLED VCC	OLED Power
GND	OLED GND	OLED Ground
3.3V	ADS1115 VCC	ADS Power
GND	ADS1115 GND	ADS Ground
✅ OLED & ADS1115 share the same I2C bus — that’s totally fine!

✅ 2. Photodiodes → ADS1115 Analog Inputs
Photodiode	Connects To
Photodiode A	A0 (ADS1115)
Photodiode B	A1 (ADS1115)
GND of both PDs	GND (ESP32)
Signal side	A0/A1 via resistor (e.g. 10k pull-down optional)
🧪 BPW-Z photodiodes are analog — they output voltage based on light intensity.

✅ 3. Laser Diode HW-493
Laser Pin	Connects To
+ (VCC)	Output of MT3608 Boost (5V)
– (GND)	GND of MT3608 / ESP32
MT3608 boosts 3.3V → 5V, which your laser needs.

✅ 4. MT3608 Step-Up Module (Boost to 5V)
MT3608 Pin	Connects To
IN+	3.3V from ESP32
IN–	GND of ESP32
OUT+	Laser VCC (+5V)
OUT–	Laser GND
✅ Turn the MT3608 potentiometer slowly clockwise to increase voltage — measure it with a multimeter till it reaches 5V.

✅ 5. Power Your ESP32
Use USB cable to power your ESP32

It gives 3.3V and 5V rails as needed

You can also power from a Li-ion battery + 5V boost later



## 🚀 How to Use
1. Flash MicroPython to ESP32
2. Upload `main.py` and `web/` using Thonny/uPyCraft
3. Update SSID & PASSWORD in code
4. Connect and access via browser at IP address

## 📄 License
MIT – Open-source and open for innovation!
