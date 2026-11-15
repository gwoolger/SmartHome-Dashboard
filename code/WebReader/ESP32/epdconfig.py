# type: ignore
import machine
import time

class EPDConfig:
    def __init__(self, spi, cs, dc, rst, busy):
        self.spi = spi
        self.cs = cs
        self.dc = dc
        self.rst = rst
        self.busy = busy

    def digital_write(self, pin, value):
        pin.value(value)

    def digital_read(self, pin):
        return pin.value()

    def delay_ms(self, delaytime):
        time.sleep_ms(delaytime)

    def spi_writebyte(self, data):
        self.spi.write(bytearray([data]))

    def spi_writebyte2(self, data):
        self.spi.write(data)
