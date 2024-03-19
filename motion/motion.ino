#include <WiFi.h>
#include <Arduino.h>

// Other LD2420 configuration variables
// const unsigned long presenceTimeout = 120000; // 120s in milliseconds
// const int minGateDistance = 1;
// const int maxGateDistance = 12;
// const float gateStillSensitivity = 0.5;
// const float gateMoveSensitivity = 0.5;

// Define pin numbers for LD2420 sensor
#define LD2420_PRESENCE_PIN 10

// Constants for radar sensor
#define RADAR_SERIAL_BAUD 9600
#define RADAR_SERIAL_TIMEOUT 1000 // Timeout in milliseconds
#define RADAR_SERIAL_RX_PIN 20     // RX pin for the radar sensor

// Timo's WiFi credentials
// const char* ssid = "TimoGS21";
// const char* password = "eueo9438";
// const char* serverAddress = "192.168.40.194";

// Timo's WiFi credentials
const char* ssid = "aced7hs";
const char* password = "a123456b";
const char* serverAddress = "192.168.146.49"; // IP address of your Raspberry Pi Flask server

const int serverPort = 5000; // Port on which Flask server is running

// Function to check for motion detection
bool motionDetected() {
  // Variables for radar sensor data
  uint8_t bytesReceived = 0;
  const int radarDataSize = 10; // Adjust according to your radar sensor output format
  uint8_t radarData[radarDataSize];

  // Initialize the serial connection for radar sensor
  Serial1.begin(RADAR_SERIAL_BAUD, SERIAL_8N1, RADAR_SERIAL_RX_PIN);
  Serial1.setTimeout(RADAR_SERIAL_TIMEOUT); // Set timeout for reading from radar sensor

  // Read data from radar sensor
  bytesReceived = Serial1.readBytes(radarData, radarDataSize);

  // Check if data received meets motion criteria (example logic)
  // Modify this according to the data format and interpretation logic of your radar sensor
  for (int i = 0; i < radarDataSize; i++) {
    // Assuming non-zero value indicates motion
    // 254 is a good threshold
    if (radarData[i] > 254.5) {
      return true; // Motion detected
    }
  }
  return false; // No motion detected
}

void setup() {
  // Initialize serial communication
  Serial.begin(115200);
  delay(1000);
  
  // Set the Presence Signal Output pin
  pinMode(LD2420_PRESENCE_PIN, INPUT_PULLUP);

  // Connect to WiFi network
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to WiFi");
}

void loop() {
  int val;
  // Send motion value to Flask server
  if (WiFi.status() == WL_CONNECTED) {
    WiFiClient client;
    if (client.connect(serverAddress, serverPort)) {
      // Check for motion detection
      if (motionDetected()) {
        val = 1;
        Serial.println("Motion detected!");
      } else {
        val = 0;
        Serial.println("No motion detected!");
      }
      String postData = "movement=" + String(val);
      client.println("POST /api/motion HTTP/1.1");
      client.println("Host: " + String(serverAddress));
      client.println("Content-Type: application/x-www-form-urlencoded");
      client.print("Content-Length: ");
      client.println(postData.length());
      client.println();
      client.println(postData);
      Serial.print("Sent to flask");
    }

    // Delay before next iteration
    delay(2000);
  }
}