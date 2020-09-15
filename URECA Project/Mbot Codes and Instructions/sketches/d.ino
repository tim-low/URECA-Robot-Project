#include <MeCore.h>

MeDCMotor motor1(M1);
MeDCMotor motor2(M2);

void setup(){}

void loop()
{
  //motor.run() maximum speed is 255 to -255, 0 is stop
  motor1.run(-100);  //Motor1 (Left) forward is -negative
  motor2.run(100);  //Motor2 (Right) forward is +positive
  delay(500);

  //motor.run() maximum speed is 255 to -255, 0 is stop
  motor1.run(100);  //Motor1 (Left) forward is -negative
  motor2.run(-100);  //Motor2 (Right) forward is +positive
  delay(500);

  motor1.stop();
  motor2.stop();
  delay(500);
}
