# Code to run on the Pi to fetch a website, and turn it into greyscale.
# Would not run on esp32 due to lack of processing power and ram.

# will try and implement scrolling and article selection with the sound pad from week 3
# (essentially reprogram it to be like a macro pad/keyboard) - though started looking at how
# id code scrolling, and it looks to be a pain, so may try partial refreshes, or might just
# get it to get single page segments at once.

# Only needs chromium, Pillow and Serial.

import subprocess
import serial
from PIL import Image


subprocess.run([                                                # headless chromium i think is the best way to do this
    "chromium", "--headless", "--no-sandbox", "--disable-gpu",
    "--window-size=400,300", "--screenshot=page.png",
    "https://bbc.co.uk/news"
])


img = Image.open("page.png").convert("L").convert("1")          # suprised greyscale converting was this easy
# img.save("preview.png")


with serial.Serial("/dev/serial0", 115200) as ser:              
    ser.write(b"SYNC" + img.tobytes())                          # Also thought this would me mubh harder

print("Sent")
