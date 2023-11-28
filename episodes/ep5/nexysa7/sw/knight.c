#include "matrak.h"

#define HIGH 1
#define LOW 0

void main(void) {

   while (1) {
      for (int i = 0; i < 8; i++) {
         gpio_write(i, HIGH);
         delay_ms(100);
         gpio_write(i, LOW);
      }
      for (int j = 7; j > -1; j--) {
         gpio_write(j, HIGH);
         delay_ms(100);
         gpio_write(j, LOW);
      }
   }
}
