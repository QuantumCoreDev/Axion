# axion_music_extractor.py
import serial
from midiutil import MIDIFile
import time

# 🔌 Configure your port
PORT = 'COM4'  # 👉 Replace with your actual COM port (e.g. COM3, COM5, /dev/ttyUSB0)
BAUD = 9600

# 🎼 Mapping entropy characters to MIDI notes
mapping = {
    '1': 60, '2': 62, '3': 64, '4': 65, '5': 67,
    '6': 69, '7': 71, '8': 72, '9': 74,
    'A': 76, 'B': 77, 'C': 79, 'D': 81,
    'E': 83, 'F': 84, 'G': 86, 'H': 88, 'I': 89
}

# 🎛️ Create MIDI File
mf = MIDIFile(1)
track = 0
time_pos = 0
channel = 0
duration = 1
volume = 100

mf.addTrackName(track, time_pos, "Axion Quantum Music")
mf.addTempo(track, time_pos, 120)

print(f"🎶 Listening to Axion on {PORT}... Press Ctrl+C to stop.")

try:
    with serial.Serial(PORT, BAUD, timeout=1) as ser:
        while True:
            char = ser.read().decode('utf-8').strip()
            if char in mapping:
                note = mapping[char]
                mf.addNote(track, channel, note, time_pos, duration, volume)
                print(f"🎵 Note {note} from entropy '{char}' at time {time_pos}")
                time_pos += 1
            if time_pos >= 100:  # Limit to 100 notes
                break
except KeyboardInterrupt:
    print("\n⏹️ Interrupted by user.")
except Exception as e:
    print(f"❌ Error: {e}")

# 💾 Save the MIDI file
filename = "Axion_Music.mid"
with open(filename, 'wb') as outf:
    mf.writeFile(outf)

print(f"\n✅ Saved MIDI file as '{filename}'")
