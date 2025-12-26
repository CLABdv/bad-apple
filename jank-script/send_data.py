#!/usr/bin/python
import usb.core
import usb.util
from time import sleep

def send_bulk_data_to_usb(id_vendor, id_product, endpoint_out):
    # Find the USB device
    dev = usb.core.find(idVendor=id_vendor, idProduct=id_product)

    if dev is None:
        print("Device not found!")
        return

    # Detach kernel driver if necessary (Linux only)
    try:
        if dev.is_kernel_driver_active(0):
            dev.detach_kernel_driver(0)
    except (usb.core.USBError, AttributeError):
        pass

    # Set the active configuration
    dev.set_configuration()

    # Perform the bulk transfer
    try:
        # USB bulk transfer
        for i in range(0, 17):
            file_name = f"alldat/alldat_{i}.dat"
            f=open(file_name, "rb")
            bulk_data = bytearray(f.read())
            f.close()
            bytes_written = dev.write(endpoint_out, bulk_data, timeout=5000)  # 5-second timeout
            print(f"Successfully sent {bytes_written} bytes to the device.")
    except usb.core.USBError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # USB device details
    ID_VENDOR = 0x0483  # Replace with your USB device's Vendor ID
    ID_PRODUCT = 0x5740  # Replace with your USB device's Product ID

    # Bulk OUT endpoint (e.g., 0x01 for OUT endpoint 1)
    BULK_OUT_ENDPOINT = 0x01
    send_bulk_data_to_usb(ID_VENDOR, ID_PRODUCT, BULK_OUT_ENDPOINT)

    # Send the data to the USB device

