# SmartHome Dashboard

This is a project that will have an eink display - monochrome for best refresh rate. An MCU for low power things, and a SBC for running home assistant style things.

## Current Status

### Wiring Schematic

This is the current wiring shematic for everything. Power will be provided to the Pi's onboard port, with the ESP32 being wired up to the Pi's 5V pin.

![Schematic](images/Schematic_v1.png)

Current Pinouts:
---
|ESP32 C6||
| - | - |
| D0 D1, D2 | empty |
| D3/21 | CS |
| D4/22 | DC |
| D5/23 | RST |
| D6/16 | TX |
| D7/17 | RX |
| D8/19 | SCK |
| D9/20 | BUSY |
| D10/18 | MOSI |

|Pi||
|-|-|
| 8/14 | TX (Connects to ESP RX) |
| 10/15 | RX (Connects ESP TX) |

### Display

Everything will be build around and for a 4.2" Black and White 400x300 E ink display

The one I have chosen is the AliExpress WeAct Eink bw display

![eink](images/eink.png)

### Raspberry Pi 3 B (1gb)

Will be using a Raspberry Pi 3 B 1gb, as it is the cheapest SBC that I can find that can run Home Assistant.

![Rpi3b](images/rpi3b.jpg)

### Xiao ESP32 C6

Chosed for it's Zigbee/Thread capabilities, decent performance, and cheap-ish price.

## Project Info
### Rough Parts

- WeAct 4.2" epaper display
- Xiao ESP32 C6
- Raspberry Pi 3 B 1gb
- 64gb Micro SD card
- Power bank with passthrough and suitable wattage output
- USB Solar Panel


### Features

An E ink display for low power dashboard data. Will pair with a Sound Pad from week 3, recoded for controls. And will be used to automate fully the curtain opener project developed in weeks 1 and 2.

Will ideally be able to run both off grid and on grid, with the power bank acting as a ups style backup. Am going to acknowledge here that likely won't work purely on solar. But can hope...

### Possibly...
Originally wanted to make the solar panel track the sun, but the added cost for servos etc probably isn't worth it, especially as the panel likely won't be able to sustain the board indefinitely.

Also did find a decent looking 7.5" e ink panel on AliExpress for $25, but that was bwr, so would have a stupid long refresh rate. But could be good for people who don't want dynamically updating info.

Was also going to make a custom Battery system, but it ended up costing more - actually only about $5 above the limit (I spent way too long looking at Aliexpress). That would have involved battery charging boards etc, as well as MOSFETs to open or close charging and power paths.

Was also hoping to get a more powerful MCU, but the ESP32 S3 doesnt have Zigbee or Thread support, and the ESP32 S31 that does costs more than the Pi.