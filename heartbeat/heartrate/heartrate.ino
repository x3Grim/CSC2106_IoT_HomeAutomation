#include "Arduino.h"
#include <60ghzbreathheart.h>

// Use Serial1 for ESP32C3 UART communication
BreathHeart_60GHz radar(&Serial1);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial1.begin(115200, SERIAL_8N1, 20, 21); // Initialize Serial1 for ESP32C3 with RX on pin 20 and TX on pin 21

  while (!Serial); // Wait for serial monitor to open
  Serial.println("Ready");
}

void loop()
{
  // put your main code here, to run repeatedly:
  radar.Breath_Heart(); // Breath and heartbeat information output

  if (radar.sensor_report != 0x00) {
      Serial.print("Sensor monitored the current heart rate value is: ");
      Serial.println(radar.heart_rate, DEC);
      Serial.println("----------------------------");
  }
  delay(500); // Add time delay to avoid program jam
}

