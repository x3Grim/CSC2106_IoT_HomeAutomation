// Include required libraries
#include "Arduino.h"

// Define pin numbers for serial communication
#define LD2420_RX_PIN 20
#define LD2420_TX_PIN 21
#define LD2420_PRESENCE_PIN 5

// Create a HardwareSerial object to communicate with the LD2420 sensor
HardwareSerial ld2420Serial(1); // Use Serial1 for ESP32C3 Super Mini

void setup() {
  // Initialize serial communication
  Serial.begin(115200);
  ld2420Serial.begin(115200, SERIAL_8N1, LD2420_RX_PIN, LD2420_TX_PIN);

  // Set the Presence Signal Output pin
  pinMode(LD2420_PRESENCE_PIN, INPUT);

  // Initialize LD2420 sensor
  initializeLD2420();
}

void loop() {
  // Check for motion detection
  if (motionDetected()) {
    Serial.println("Motion detected!");
  }

  // Delay before next iteration
  delay(1000);
}

// Function to initialize LD2420 sensor
void initializeLD2420() {
  // Send any initialization commands if needed
  // For example, setting operating mode
  // You can send commands via UART to configure the sensor
  Serial.println("Initialize!");
}

// Function to check for motion detection
bool motionDetected() {
  // Check for presence signal from LD2420 sensor
  if (digitalRead(LD2420_PRESENCE_PIN) == LOW) {
    return true;
  }
  return false;
}
