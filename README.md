# Axion: Quantum Physics Hardware Simulator

**Created by Pushkar (QuantumCoreDev)**

Axion is a cutting-edge open-source quantum hardware simulator that brings four foundational quantum physics experiments to life — now upgraded with a **fifth mode** that converts quantum entropy into real **music**!

---

## 🔬 Key Experiments

1. **Quantum Random Number Generator (QRNG)**
2. **Polarization Explorer (Malus's Law)**
3. **Photoelectric Effect Simulator**
4. **Mach–Zehnder Interferometer (MZI)**
5. **Quantum Music Synth 🎵** *(NEW!)*

Each experiment is built using real sensors, light sources, and an Arduino UNO Mini, housed in a 25x15x5 cm chassis.

---

## 📸 Hardware Components

| Component                  | Qty | Description                          |
|---------------------------|-----|--------------------------------------|
| Arduino UNO Mini          | 1   | ABX00062 official                    |
| OLED Display (SSD1306)    | 1   | 128x64 I2C screen                    |
| Photodiodes               | 3   | Light detection                      |
| Red Laser Modules         | 2   | Used in PE & MZI                     |
| IR LED                    | 1   | Optional alternate path              |
| LDR / Light Sensor        | 1   | Backup/visual                        |
| Polarizing Film           | 2   | For Malus’s Law                      |
| Beamsplitters             | 2   | For MZI                              |
| Servo Motors (SG90)       | 2   | Polarizer/Mirror rotation            |
| Button                    | 1   | Mode selector                        |
| Resistors (10k)           | 2–3 | Voltage divider                      |
| Breadboard + Wires        | —   | Prototyping                          |
| Battery / USB Power       | 1   | 3.7V/9V or USB                       |

---

## 🧠 How It Works

Each press of the button cycles Axion through the following experiments:

| Mode | Experiment                    | Output                               |
|------|-------------------------------|--------------------------------------|
| 0    | QRNG                          | OLED & Serial – Random Bits/Bytes    |
| 1    | Polarization Explorer         | OLED – Angle vs Intensity            |
| 2    | Photoelectric Effect          | OLED – Emitted Electron Energy       |
| 3    | Mach–Zehnder Interferometer   | OLED – Light Interference Patterns   |
| 4    | Quantum Music Synth 🎶        | Serial – Entropy to MIDI             |

---

## 🎵 Quantum Music Synth (Mode 4)

> **Hear the universe’s randomness.** This mode transforms real quantum entropy into generative ambient music using MIDI.

### 🧬 Concept

This experiment uses analog noise from a photodiode (QRNG module) to output entropy characters (`1–9`, `A–I`). These characters are mapped to musical notes and rendered into a `.mid` file — letting you *hear randomness* as cosmic-sounding audio.

### ⚙️ How It Works

1. Arduino reads noisy photodiode values (`analogRead` from pin A0).
2. Values are mapped to entropy characters:
   `'1'–'9' → MIDI notes 60–74`, `'A'–'I' → MIDI notes 76–89`
3. Characters are streamed via Serial.
4. A Python script converts these into a MIDI file.

### 💻 How To Use

#### Step 1: Switch to Mode 4
- Press the button on Axion until OLED shows:
  ```
  Quantum Music
  Entropy: X
  ```

#### Step 2: Run Python MIDI Extractor
```bash
pip install pyserial midiutil
python python/axion_music_extractor.py
```
This will create a file:
```bash
Axion_Music.mid
```

### 🎧 Play the Music
Open `Axion_Music.mid` in:
- [🎼 Online Sequencer](https://onlinesequencer.net)
- 🎹 Audacity / LMMS / Sonic Pi
- 🎛️ Any DAW or MIDI Player

### 🛠️ Advanced Ideas
- Real-time MIDI via `pygame.midi`
- Scale mapping (Raag Bhairavi, Lydian, etc.)
- Multi-channel entropy layering for harmony

---


## 📜 License
MIT License — Free to use, remix, and expand.

---

## 🌐 Connect
**Pushkar (QuantumCoreDev)**  
GitHub: [@QuantumCoreDev](https://github.com/QuantumCoreDev)  
> If you're from Google X, Microsoft Research, or an IIT — reach out. Let's take Axion global. 🌍
