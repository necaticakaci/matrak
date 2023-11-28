// Matrak Çevrebirim Kütüphanesi

#include <stdint.h>

#define GPIO0_BASE (0x80001000U)
#define GPIO0 ((GPIO*) GPIO0_BASE)

#define UART0_BASE (0x80002000U)
#define UART0 ((UART*) UART0_BASE)

#define CYC_C0_BASE (0x80003000U)
#define CYC_C0 ((CYC_C*) CYC_C0_BASE)

#define CLK_FREQ 50000000

typedef struct {
  volatile uint32_t gpio_output;  // 0x80001000 (RW) OUTPUT REGISTER
} GPIO;

typedef struct {
  volatile uint32_t uart_transmit;  // 0x80002000 (W) TX DATA REGISTER
  volatile uint32_t uart_status;    // 0x80002004 (R) TX STATUS REGISTER
} UART;

typedef struct {
  volatile uint32_t clock_counter;  // 0x80003000 (R) CLOCK COUNTER REGISTER
} CYC_C;

void gpio_write(int gpio_pin, int value) {
   if (value) {
      GPIO0->gpio_output |= (1<<gpio_pin);
   }
   else {
      GPIO0->gpio_output &= ~(1<<gpio_pin);
   }
}

void delay_ms(int time) {
   uint32_t clk_value = CYC_C0->clock_counter + (time * CLK_FREQ) / 1000;
   while (CYC_C0->clock_counter < clk_value);
}

void put_char(int c) {
   uint32_t done = 0;
   UART0->uart_transmit = c;
   while (done == 0) {
      done = UART0->uart_status;
   }
}

void put_str(const char* s) {
   for (const char* p=s; *p; ++p) {
      put_char(*p);
   }
}
