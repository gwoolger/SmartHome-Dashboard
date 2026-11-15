# type: ignore

import machine


# For the ESP32-C6, UART0 corresponds to D6 and D7 for TX and TX.
# 115200 should be plenty. as only sending json.

uart = machine.UART(0, baudrate=115200)

print("ESP32-C6 Booted Successfully.")
