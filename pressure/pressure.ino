#include <WiFi.h>

const char* ssid = "ssid";
const char* password = "password";
const char* serverAddress = "192.168.146.49"; // IP address of your Raspberry Pi Flask server
const int serverPort = 5000; // Port on which Flask server is running

void setup() {
  Serial.begin(9600);
  delay(1000);
  
  // Connect to WiFi network
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  int val;
  val = analogRead(0);
  
  // Send vibration value to Flask server
  if (WiFi.status() == WL_CONNECTED) {
    WiFiClient client;
    if (client.connect(serverAddress, serverPort)) {
      String postData = "vibration=" + String(val);
      client.println("POST /api/pressure HTTP/1.1");
      client.println("Host: " + String(serverAddress));
      client.println("Content-Type: application/x-www-form-urlencoded");
      client.print("Content-Length: ");
      client.println(postData.length());
      client.println();
      client.println(postData);
      Serial.print("Sent to flask");
    }
    delay(2000);
  }
}