#include "matrak.h"

#define LED_PIN 4
#define HIGH 1
#define LOW 0

void main(void) {

   while (1) {
      gpio_write(LED_PIN, HIGH);
      delay_ms(500);
      gpio_write(LED_PIN, LOW);
      delay_ms(500);
   }
}
