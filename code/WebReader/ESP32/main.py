# type: ignore
import machine
import epaper4in2

spi_bus = machine.SPI(1, baudrate=4000000, polarity=0, phase=0, sck=machine.Pin(19), mosi=machine.Pin(18))

epd_cs   = machine.Pin(21, machine.Pin.OUT) # D3/21
epd_dc   = machine.Pin(22, machine.Pin.OUT) # D4/22
epd_rst  = machine.Pin(23, machine.Pin.OUT) # D5/23
epd_busy = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_UP) # D9/20

display = epaper4in2.EPD(spi_bus, epd_cs, epd_dc, epd_rst, epd_busy)
display.init()


uart = machine.UART(0, baudrate=115200, tx=machine.Pin(16), rx=machine.Pin(17), rxbuf=16384)    # Need large rx buffer due to image
frame = bytearray(15000)

print("ESP32 Setup")

while True:
    if uart.any() >= 4:
        if uart.read(4) == b"SYNC":
            bytes_read = 0
            while bytes_read < 15000:
                chunk = uart.readinto(memoryview(frame)[bytes_read:])
                if chunk:
                    bytes_read += chunk

            print("Frame received! Updating display...")
            display.init()  # Re-init in case it was sleeping from a previous frame
            display.display_frame(frame)
            display.sleep()
            print("Done")
