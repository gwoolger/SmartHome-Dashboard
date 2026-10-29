# This code runs on the ESP32 to receive data over the serial line from the Pi and display it on the screen.
# will possible recode in C++, if performance becomes an issue


# type: ignore
import json
import time
import machine
import epaper4in2


spi_bus = machine.SPI(1, baudrate=4000000, polarity=0, phase=0, sck=machine.Pin(19), mosi=machine.Pin(18))

epd_cs   = machine.Pin(21, machine.Pin.OUT) # D3/21
epd_dc   = machine.Pin(22, machine.Pin.OUT) # D4/22
epd_rst  = machine.Pin(23, machine.Pin.OUT) # D5/23
epd_busy = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_UP) # D9/20


display = epaper4in2.EPD(spi_bus, epd_cs, epd_dc, epd_rst, epd_busy)


uart = machine.UART(0, baudrate=115200, tx=machine.Pin(16), rx=machine.Pin(17))     # definine UART for pi comms

print("UART Active. Listening to Pi Serial")

while True:
    # Read incoming data directly from the physical UART bus pins
    if uart.any():
        raw_line = uart.readline()
        if raw_line:
            clean_line = raw_line.decode('utf-8').strip()   # idk if i need this
            
            # JSON
            payload = json.loads(clean_line)
            room_temp = payload.get("temp", 0.0)
            system_batt = payload.get("batt", 0)
            
            print(f"Synced -> Temp: {room_temp}C | Battery: {system_batt}%")
            
            # epaper. hopefully correct corrdinates. dont have screen to test.
            display.fill(1) # Am hoping this is inherited from framebuf, as if not will not work
            display.text("SMARTHOME DASHBOARD", 20, 20, 0)
            display.text(f"Room Temp:  {room_temp} C", 20, 60, 0)
            display.text(f"Battery:    {system_batt}%", 20, 90, 0)
            display.show()
                

    time.sleep(0.1)  # Wont refresh screen, as waits for uart.any
