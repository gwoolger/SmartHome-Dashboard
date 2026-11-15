# This code runs on the Pi to transmit data over the serial line for the ESP32 to display on the screen.

import json
import time
import serial

SERIAL_PORT = '/dev/serial0'  # Pi3B default
BAUD_RATE = 115200  # Could do higher, like 921.6k, but not needed


def get_data():
    '''Gets the Data from Home Assistant'''

    # Could implement a call to Home Assistant here, as doesnt seem too hard, but no real point yet

    return {"temp": 21.5, "hum": 60, "batt": 88}

def main():
    '''Main function to run the code'''

    # Opens the serial port
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

    while True:
        data = get_data()
        json_data = json.dumps(data) + "\n"
        ser.write(json_data.encode('utf-8')) # sedn
        time.sleep(60)  # 60 seconds is probably too fast anyway




if __name__ == "__main__":
    main()
