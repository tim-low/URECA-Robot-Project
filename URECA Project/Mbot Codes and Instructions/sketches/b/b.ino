#include <MeMCore.h>
MeBuzzer buzzer;

void setup(){
  buzzer.tone(600, 1000);  //Buzzer sounds at 600hz for 1000ms
  delay(2000);
  buzzer.tone(1200, 1000);  //Buzzer sounds at 1200hz for 1000ms
  delay(2000);
}
