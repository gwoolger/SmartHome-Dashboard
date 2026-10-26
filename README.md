# SmartHome Dashboard

This is a project that will have an eink display - monochrome for best refresh rate. An MCU for low power things, and a SBC for running home assistant style things.

## Project Plans
### Cost
This will ideally cost less than $100, as I will be aiming for the tier 3 grant of half life, so I can maximise the screen size.

It will not however include battery cells (standard 18650s), as they are too expensive to include (and I also already have some).

### Rough parts

- E ink display
- MCU, probably an esp32s3
- SBC, likely a pi 3 b 1gb, as will actually fit in budget and be in stock. but could easily be upgraded to any later pi models. Though the 1gb of ram could be interesting if I try to run home assistant on it
- Batt system: BMS, charger etc
- Solar system: solar panels, solar charger
- Might make a 3d printed case. Or just make one of of card at assembly time

### Features

An E ink display for low power dashboard data. Will pair with a Sound Pad from week 3, recoded for controls. And will be used to automate fully the curtain opener project developed in weeks 1 and 2.

Will ideally be able to run both off grid and on grid, with the batteries acting as a ups style backup. Am going to acknowledge here that likely won't work purely on solar. But can hope...

### Possibly...
Originally wanted to make the solar panel track the sun, but the added cost for servos etc probably isn't worth it, especially as the panel likely won't be able to sustain the board indefinitely.

Also did find a decent looking 7.5" e ink panel on AliExpress for $25, but that was bwr, so would have a stupid long refresh rate. But could be good for people who don't want dynamically updating info.
