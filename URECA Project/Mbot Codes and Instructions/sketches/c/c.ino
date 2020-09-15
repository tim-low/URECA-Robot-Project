#include "MeMCore.h"

#define red        255,000,000
#define blue       000,000,255

MeRGBLed led(PORT_7, 2);  
                             
void setup()
{
}

void loop()
{
  led.setColorAt (0, blue);
  led.setColorAt (1, red);
  led.show();
  delay (100);
  led.setColorAt (0, red);
  led.setColorAt (1, blue);
  led.show();
  delay (100);
}
