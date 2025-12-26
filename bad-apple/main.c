#include "main.h"
#include "frames/compressed.h"
#include <libopencm3/stm32/gpio.h>
#include <libopencm3/stm32/rcc.h>
#include <libopencm3/usb/cdc.h>
#include <libopencm3/usb/usbd.h>
#include <stdint.h>

#include "clock.h"
#include "lcd.h"
#include "libopencm3/stm32/f4/gpio.h"
#include "sdram.h"

static void gpio_setup(void) {
  rcc_clock_setup_pll(&rcc_hse_8mhz_3v3[RCC_CLOCK_3V3_168MHZ]);
  rcc_periph_clock_enable(RCC_GPIOA);
  rcc_periph_clock_enable(RCC_GPIOG);

  gpio_mode_setup(GPIOG, GPIO_MODE_OUTPUT, GPIO_PUPD_NONE, GPIO13 | GPIO14);
  gpio_mode_setup(GPIOA, GPIO_MODE_AF, GPIO_PUPD_NONE, GPIO9 | GPIO10);
  gpio_set_af(GPIOA, GPIO_AF7, GPIO9 | GPIO10);
}

uint8_t *sdram_ptr = SDRAM_BASE_ADDRESS + 2 * LCD_HEIGHT * LCD_WIDTH * 2;

int main(void) {
  clock_setup();
  gpio_setup();
  sdram_init();
  lcd_init();

  /*for (unsigned int i = 0;
       i < sizeof(compressed_frame_0) / sizeof(compressed_frame_0[0]); i++) {*/
  int tot_pixels = 0;
  while (1) {
    int i = 0;
    int white = compressed_frame_0[i] & 0x80;   // highest bit
    int npixels = compressed_frame_0[i] & 0x7f; // all bits except highest
    if (white) {
      for (int j = 0; j < npixels; j++) {
        int tmp = tot_pixels + j;
        lcd_draw_pixel_1d(tmp, LCD_CYAN);
        if (tmp == LCD_HEIGHT * LCD_WIDTH - 1) {
          gpio_toggle(GPIOG, GPIO13);
          lcd_show_frame();
          tot_pixels = 0;
        }
      }
    } else {
      for (int j = 0; j < npixels; j++) {
        int tmp = tot_pixels + j;
        lcd_draw_pixel_1d(tmp, LCD_BLUE);
        if (tmp == LCD_HEIGHT * LCD_WIDTH - 1) {
          gpio_toggle(GPIOG, GPIO13);
          lcd_show_frame();
          tot_pixels = 0;
        }
      }
    }
    tot_pixels += npixels;
    // lcd_show_frame();
    ++i;
  }

  return 0;
}
