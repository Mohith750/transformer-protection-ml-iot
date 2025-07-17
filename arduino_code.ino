
#include <DHT.h>
#define DHTPIN 2     
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float temp = dht.readTemperature();
  int current = analogRead(A0);  // Simulated
  int voltage = analogRead(A1);  // Simulated

  Serial.print(temp);
  Serial.print(",");
  Serial.print(current);
  Serial.print(",");
  Serial.println(voltage);

  delay(1000);  // Read every second
}
