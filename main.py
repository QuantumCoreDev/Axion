
# Axion – Quantum RNG with OLED + Web Dashboard
from machine import I2C, Pin
from ads1x15 import ADS1115
import ssd1306
import network, socket, time

# === I2C Setup ===
i2c = I2C(1, scl=Pin(22), sda=Pin(21))

# === OLED Init ===
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# === ADS1115 Init ===
ads = ADS1115(i2c, addr=0x48, gain=1)

# === Wi-Fi Setup ===
SSID = 'Your_SSID'
PASSWORD = 'Your_PASSWORD'

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        time.sleep(0.5)
    print("Wi-Fi Connected:", wlan.ifconfig()[0])
    return wlan.ifconfig()[0]

def read_photodiodes():
    return ads.read(0), ads.read(1)

def get_raw_bit():
    a, b = read_photodiodes()
    return 1 if a > b else 0 if b > a else None

def get_random_bit():
    while True:
        b1, b2 = get_raw_bit(), get_raw_bit()
        if b1 is None or b2 is None: continue
        if b1 == 1 and b2 == 0: return 1
        elif b1 == 0 and b2 == 1: return 0

def update_oled(bits):
    oled.fill(0)
    oled.text("Axion QRNG", 0, 0)
    oled.text("Entropy:", 0, 10)
    for i in range(2):
        oled.text(bits[i*32:(i+1)*32], 0, 20 + i*10)
    oled.show()

def web_page(bits):
    return f"""
<html><head><meta http-equiv='refresh' content='2'><style>
body {{ background: black; color: lime; font-family: monospace; text-align: center; }}
</style></head><body>
<h1>Axion QRNG</h1><p>{bits}</p></body></html>"""

def start_server():
    s = socket.socket()
    s.bind(('', 80))
    s.listen(1)
    print("Web server running on port 80")
    while True:
        conn, addr = s.accept()
        bits = ''.join(str(get_random_bit()) for _ in range(64))
        update_oled(bits)
        conn.sendall('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')
        conn.sendall(web_page(bits))
        conn.close()

ip = connect_wifi()
print("Server running at:", ip)
start_server()
