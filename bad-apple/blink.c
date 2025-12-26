#include <libopencm3/stm32/rcc.h>
#include <libopencm3/stm32/gpio.h>

static void gpio_setup(void)
{
    rcc_periph_clock_enable(RCC_GPIOG);
    gpio_mode_setup(GPIOG, GPIO_MODE_OUTPUT, GPIO_PUPD_NONE, GPIO13 | GPIO14);
}

int main(void) {
    gpio_setup();
    gpio_set(GPIOG, GPIO13);
    while(1)
    {
        for(int i = 0; i < 1000000; i++)
        {
            __asm__("nop");
        }
        gpio_toggle(GPIOG, GPIO13);
        gpio_toggle(GPIOG, GPIO14);
    }
    return 0;
}
