// Read temperature and display it in serial
const int tempSensor = A0;



void setup() {
  Serial.begin(9600);

}

void loop() {

  int sensorVal = analogRead(tempSensor);

  // Convert the sensorvalue into voltage, value between 0 - 5
  float voltageValue = (sensorVal/1024.0) * 5.0;

  // Convert the voltage into temperature in degrees celsius
  float temperature = (voltageValue - 0.5) * 100;

  Serial.println(temperature);

}
