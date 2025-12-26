#!/usr/bin/python
import usb.core
import usb.util
from time import sleep

def send_usb_message(id_vendor, id_product, bm_request_type, b_request, w_value, w_index, message):
    # Find the USB device
    dev = usb.core.find(idVendor=id_vendor, idProduct=id_product)

    if dev is None:
        print("Device not found!")
        return

    # Detach kernel driver if necessary (Linux only)
    try:
        if dev.is_kernel_driver_active(0): # type: ignore
            dev.detach_kernel_driver(0) # type: ignore
    except (usb.core.USBError, AttributeError):
        pass

    try:
        # Perform a control transfer
        dev.ctrl_transfer( # type: ignore
            bmRequestType=bm_request_type,
            bRequest=b_request,
            wValue=w_value,
            wIndex=w_index,
            data_or_wLength=message
        )
        print("Message sent successfully!")
    except usb.core.USBError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # USB device details
    ID_VENDOR = 0x0483
    ID_PRODUCT = 0x5740

    # Control transfer parameters
    BM_REQUEST_TYPE = 0x41
    B_REQUEST = 0x33
    W_VALUE = 1
    W_INDEX = 0

    # The message to send
    MESSAGE = b"Hello USB"

    # Send the message
    while(1):
        W_VALUE ^= 1
        send_usb_message(ID_VENDOR, ID_PRODUCT, BM_REQUEST_TYPE, B_REQUEST, W_VALUE, W_INDEX, MESSAGE)
        sleep(0.1)
        

