#include <MeMCore.h>

MeRGBLed led(0, 30);
MeIR ir; 
MeDCMotor motor1(M1); //Motor1 is Left Motor
MeDCMotor motor2(M2); //Motor2 is Right Motor
MeUltrasonicSensor ultrasonic(PORT_3);


void setup()
{
    led.setpin(13);
    
    ir.begin();
    Serial.begin(9600);
}

void loop()
{
    if(ir.decode())
    {
      uint32_t value = ir.value;
      value = value >> 16 & 0xff;
      Serial.print("Button Code: ");
      Serial.println(value);
      delay(250);
      switch(value)
        {
            case IR_BUTTON_A: led.setColor(255, 255, 255); //Set both LED to White
                              led.show();                  //Must use .show() to make new colour take effect
                              break;
            
            case IR_BUTTON_B: led.setColor(0, 0, 0); //Set both LED to White
                              led.show();                  //Must use .show() to make new colour take effect
                              break;
            
            case IR_BUTTON_C: motor1.run(0); //Motor1 (Left)  forward is -negative
                                motor2.run(0);  //Motor2 (Right) forward is +positive
                                break;
            
            case IR_BUTTON_D: Serial.println("D");break;
            case IR_BUTTON_E: Serial.println("E");break;
            case IR_BUTTON_F: Serial.println("F");break;
            case IR_BUTTON_SETTING : Serial.println("Setting");break;
            
            case IR_BUTTON_LEFT:    motor1.run(100); //Motor1 (Left)  forward is -negative
                                    motor2.run(100);  //Motor2 (Right) forward is +positive
                                    break;
            
            case IR_BUTTON_RIGHT:   motor1.run(-100); //Motor1 (Left)  forward is -negative
                                    motor2.run(-100);  //Motor2 (Right) forward is +positive
                                    break;
            
            case IR_BUTTON_UP:      motor1.run(-100); //Motor1 (Left)  forward is -negative
                                    motor2.run(100);  //Motor2 (Right) forward is +positive
                                    break;

            case IR_BUTTON_DOWN:    motor1.run(100); //Motor1 (Left)  forward is -negative
                                    motor2.run(-100);  //Motor2 (Right) forward is +positive
                                    break;
            
            case IR_BUTTON_0: Serial.println("0");break;
            
            case IR_BUTTON_1:       
                                    int speed = 100;
                                    int turnTime = 2750;
                                    int maxDistance = 18;
                                    int state = 0;
                                    while (true) {
                                      
                                      if (ultrasonic.distanceCm() > maxDistance){
                                        motor1.run(-100); //Motor1 (Left)  forward is -negative
                                        motor2.run(100);  //Motor2 (Right) forward is +positive
                                      }

                                      if (state==0 && ultrasonic.distanceCm() < maxDistance){
                                         motor1.run(100); //Motor1 (Left)  forward is -negative
                                         motor2.run(100);  //Motor2 (Right) forward is +positive
                                         delay(turnTime/4);
                                         if (ultrasonic.distanceCm() < maxDistance){
                                          state++;
                                         }
                                         else state=0;
                                      }
                                      if (state==1 && ultrasonic.distanceCm() < maxDistance){
                                         motor1.run(-100); //Motor1 (Left)  forward is -negative
                                         motor2.run(-100);  //Motor2 (Right) forward is +positive
                                         delay(turnTime/2);
                                         if (ultrasonic.distanceCm() < maxDistance){
                                          state++;
                                         }
                                         else state=0;
                                      }
                                      if (state==2 && ultrasonic.distanceCm() < maxDistance){
                                         motor1.run(-100); //Motor1 (Left)  forward is -negative
                                         motor2.run(-100);  //Motor2 (Right) forward is +positive
                                         delay(turnTime/4);
                                         if (ultrasonic.distanceCm() < maxDistance){
                                          state++;
                                         }
                                         else state=0;
                                      }
                                      if (state==3 && ultrasonic.distanceCm() < maxDistance){
                                         motor1.run(-100); //Motor1 (Left)  forward is -negative
                                         motor2.run(-100);  //Motor2 (Right) forward is +positive
                                         delay(turnTime/8);
                                         if (ultrasonic.distanceCm() < maxDistance){
                                          state=0;
                                         }
                                      }
                                      if(ir.decode()){
                                        stopmovement();
                                        break;
                                      }
                                    }
                                    break;
                                    
            case IR_BUTTON_2: Serial.println("2");break;
            case IR_BUTTON_3: Serial.println("3");break;
            case IR_BUTTON_4: Serial.println("4");break;
            case IR_BUTTON_5: Serial.println("5");break;
            case IR_BUTTON_6: Serial.println("6");break;
            
            case IR_BUTTON_7:       motor1.run(80); //Motor1 (Left)  forward is -negative
                                    motor2.run(80);  //Motor2 (Right) forward is +positive
                                    delay(4445);
                                    stopmovement();
                                    break;
            
            case IR_BUTTON_8:       motor1.run(100); //Motor1 (Left)  forward is -negative
                                    motor2.run(100);  //Motor2 (Right) forward is +positive
                                    delay(687);
                                    stopmovement();
                                    break;
            
            case IR_BUTTON_9:       motor1.run(200); //Motor1 (Left)  forward is -negative
                                    motor2.run(200);  //Motor2 (Right) forward is +positive
                                    delay(1255);
                                    stopmovement();
                                    break;

            default:break;
        }
    }
}

void stopmovement(){
  motor1.run(0); //Motor1 (Left)  forward is -negative
  motor2.run(0);  //Motor2 (Right) forward is +positive
}

//ultrasonic.distanceCm()
