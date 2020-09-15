#include "MeMCore.h"

// create an object named ultrasensor 
MeUltrasonicSensor ultraSensor(PORT_1); 

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  Serial.print("Distance : ");
  Serial.print(ultraSensor.distanceInch() );  //or distanceCm()
  Serial.printInch(" inch");
  delay(100);
}
