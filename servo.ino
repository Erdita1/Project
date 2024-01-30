#include <Servo.h>

Servo servoMotor;
int servoPin = 11;        // Pin yang digunakan untuk servo motor
int potentiometerPin = A0; // Pin yang digunakan untuk potensiometer

int potValue;
int servoPos;

void setup() {
  servoMotor.attach(servoPin);
}

void loop() {
  // Baca nilai dari potensiometer (0-1023)
  potValue = analogRead(potentiometerPin);

  // Map nilai potensiometer ke rentang sudut servo (0-180)
  servoPos = map(potValue, 0, 1023, 0, 180);

  // Putar servo sesuai dengan posisi potensiometer
  servoMotor.write(servoPos);

  delay(10); // Delay kecil untuk menghindari getaran
}
