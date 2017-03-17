#include <DHT.h>
#include <Bridge.h>

#define DHTPIN 2     // what digital pin we're connected to

#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE);

unsigned long timer;
unsigned long counter = 0L;

void setup() {
  Serial.begin(9600);
  Serial.println("DHT11 test!");

  Bridge.begin();
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();
//  float f = dht.readTemperature(true);
//
//  // Check if any reads failed and exit early (to try again).
//  if (isnan(h) || isnan(t) || isnan(f)) {
//    Serial.println("Failed to read from DHT sensor!");
//    return;
//  }
//  
//  float hif = dht.computeHeatIndex(f, h);
//  float hic = dht.computeHeatIndex(t, h, false);

  if (millis() - timer > 200) {
        timer = millis();
        Bridge.put("temperature", String(t));
        Serial.println("temperature :" + String(t));
        Bridge.put("humidity", String(h));
        Serial.println("humidity : " + String(h));
    }
}
