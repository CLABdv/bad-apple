#ifndef CDCACM_H
#define CDCACM_H
#include <libopencm3/usb/cdc.h>
#include <libopencm3/usb/usbd.h>

usbd_device *create_usb_handle(void);
extern volatile uint8_t transmitting_data;

#endif

