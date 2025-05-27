#include <Servo.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define OLED_WIDTH 128
#define OLED_HEIGHT 64
#define OLED_RESET -1
Adafruit_SSD1306 display(OLED_WIDTH, OLED_HEIGHT, &Wire, OLED_RESET);

// Pins
#define QRNG_PIN A0
#define PE_PIN A1
#define MZI_PIN A2
#define POLAR_PIN A3
#define BTN_PIN 2
#define LASER_PE 3
#define LASER_MZI 4
#define SERVO_POLAR 5
#define SERVO_MZI 6

Servo servoPolar, servoMZI;

int mode = 0;
unsigned long lastDebounce = 0;
const int debounceDelay = 300;

void setup() {
  Serial.begin(9600);
  pinMode(BTN_PIN, INPUT_PULLUP);
  pinMode(LASER_PE, OUTPUT);
  pinMode(LASER_MZI, OUTPUT);
  digitalWrite(LASER_PE, LOW);
  digitalWrite(LASER_MZI, LOW);

  servoPolar.attach(SERVO_POLAR);
  servoMZI.attach(SERVO_MZI);

  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    while (1); // Halt
  }
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.display();
}

void loop() {
  if (digitalRead(BTN_PIN) == LOW && millis() - lastDebounce > debounceDelay) {
    mode = (mode + 1) % 4;
    lastDebounce = millis();
    display.clearDisplay();
  }

  switch (mode) {
    case 0: runQRNG(); break;
    case 1: runPolarizationExplorer(); break;
    case 2: runPhotoelectricEffect(); break;
    case 3: runMachZehnder(); break;
  }
}

void runQRNG() {
  int val = analogRead(QRNG_PIN);
  byte bit = val & 1;
  display.setCursor(0, 0);
  display.print("QRNG:");
  display.setCursor(0, 10);
  display.print("Bit: "); display.println(bit);
  display.display();
  delay(100);
  display.clearDisplay();
}

void runPolarizationExplorer() {
  for (int angle = 0; angle <= 180; angle += 10) {
    servoPolar.write(angle);
    delay(200);
    int intensity = analogRead(POLAR_PIN);
    display.setCursor(0, 0);
    display.print("Polarization");
    display.setCursor(0, 10);
    display.print("Angle: "); display.println(angle);
    display.setCursor(0, 20);
    display.print("Intensity: "); display.println(intensity);
    display.display();
    delay(400);
    display.clearDisplay();
  }
}

void runPhotoelectricEffect() {
  digitalWrite(LASER_PE, HIGH);
  delay(100);
  int voltage = analogRead(PE_PIN);
  display.setCursor(0, 0);
  display.print("Photoelectric");
  display.setCursor(0, 10);
  display.print("Voltage: "); display.println(voltage);
  display.display();
  delay(300);
  digitalWrite(LASER_PE, LOW);
  display.clearDisplay();
}

void runMachZehnder() {
  digitalWrite(LASER_MZI, HIGH);
  for (int angle = 0; angle <= 180; angle += 15) {
    servoMZI.write(angle);
    delay(150);
    int light = analogRead(MZI_PIN);
    display.setCursor(0, 0);
    display.print("MZ Interferometer");
    display.setCursor(0, 10);
    display.print("Servo: "); display.println(angle);
    display.setCursor(0, 20);
    display.print("Intensity: "); display.println(light);
    display.display();
    delay(300);
    display.clearDisplay();
  }
  digitalWrite(LASER_MZI, LOW);
}
