#include "Arduino.h"
#include <60ghzbreathheart.h>
#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "xxxx";
const char* password = "xxxx";
const char* serverAddress = "192.168.146.49"; // IP address of your Raspberry Pi Flask server
const int serverPort = 5000; // Port on which Flask server is running


// can also try hardware serial with
BreathHeart_60GHz radar = BreathHeart_60GHz(&Serial1);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial1.begin(115200, SERIAL_8N1, 20, 21); // Initialize Serial1 for ESP32C3 with RX on pin 20 and TX on pin 21

  while (!Serial); // Wait for serial monitor to open
  Serial.println("Ready");

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to WiFi");
}


int sleep_state() {
  radar.SleepInf_Decode();         
  if (radar.sensor_report != 0x00) {
    switch(radar.sensor_report){
      case OUTBED:
        Serial.println("Sensor detects someone currently leaving the bed.");
        Serial.println("----------------------------");
        return 1;
      case INBED:
        Serial.println("Sensor detects that someone is currently in bed.");
        Serial.println("----------------------------");
        return 2;
      case NOINOUT:
        Serial.println("No subject is detected leaving or going to bed.");
        Serial.println("----------------------------");
        return 3;
      case SLEEPAWAKE:
        Serial.println("Sensor detects that the monitoring people is awake.");
        Serial.println("----------------------------");
        return 4;
      case SLEEPLIGHT:
        Serial.println("Sensor detects that the monitoring people is in light sleeping.");
        Serial.println("----------------------------");
        return 5;
      case SLEEPDEEP:
        Serial.println("Sensor detects that the monitoring people is in deep sleeping.");
        Serial.println("----------------------------");
        return 6;
      case SLEEPNONE:
        Serial.println("Sleep state of the object is not detected.");
        Serial.println("----------------------------");
        return 7;
    }
  }
  else{
      Serial.println("No sleep state reported.");
      return 0;
    }
}

void loop()
{
  int val;
  val = sleep_state();

  if (WiFi.status() == WL_CONNECTED) {
    WiFiClient client;
    if (client.connect(serverAddress, serverPort)) {
      String postData = "state=" + String(val);
      client.println("POST /api/sleep HTTP/1.1");
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