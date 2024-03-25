#include "Arduino.h"

// Define pin numbers for LD2420 sensor
#define LD2420_PRESENCE_PIN 10

// Other LD2420 configuration variables
const unsigned long presenceTimeout = 120000; // 120s in milliseconds
const int minGateDistance = 1;
const int maxGateDistance = 12;
const float gateStillSensitivity = 0.5;
const float gateMoveSensitivity = 0.5;

void setup() {
  // Initialize serial communication
  Serial.begin(115200);
  
  // Set the Presence Signal Output pin
  pinMode(LD2420_PRESENCE_PIN, INPUT_PULLUP);
}

void loop() {
  // Check for motion detection
  if (motionDetected()) {
    Serial.println("Motion detected!");
  } else {
    Serial.println("No motion detected!");
  }
  
  // Delay before next iteration
  delay(1000);
}

// Function to check for motion detection
bool motionDetected() {
  // Check for presence signal from LD2420 sensor
  if (digitalRead(LD2420_PRESENCE_PIN) == LOW) {
    return true;
  }
  return false;
}