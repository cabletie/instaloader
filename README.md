# Instaloader
## Author
* @cabletie
* cabletie@pjndj.net

## Summary
Kit that downloads images from an instagram accout and displays them on an ESP32 with an LCD

## Overview of operation
* periodically a cron job on a raspberry pi downloads instagram images using the "instaloader" tool available from 
* Links newest (latest) image to latest.jpg
* Cron script converts latest.jpb to latest_135.jpg and down-scales to max 135 pixels high
* Apache service running on RPi serves these files via http
* ESP32 (TTGO T-Display module running LoBo uPython) client program periodically retrieves latest_135.jpg from the server and;
* displays it on it's connected LCD

Ultimately it'd be good to get this all working on the ESP32 to avoid using the intermediate RaspberryPi

## image scaling python script
[tools/scale.py](https://github.com/cabletie/instaloader/blob/master/tools/instaloader.sh)
* Uses PILL module to scale down to max width
* Edit the script to set the width for your LCD

## RPi cron script
[tools/instaloader.sh](https://github.com/cabletie/instaloader/blob/master/tools/scale.py)
* Runs every 5 minutes between 8 pm and 2 am (most likely time for this instagram account to be updated)
* Runs once/hour other times
* runs the main instaloader script to fetch only entries since last download
* creates a link to the latest image file
* calls the scale.py script to scale it to a usable size for the LCD

## References
### instaloader
https://github.com/instaloader/instaloader

## Loboris micropython
https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo
Note this is a really great implementation IMO but sadly doesn't seem to be being kept updated. If someone knows where all the great moduels  can be found separately, or if it's being maintained somewhere else I'd love to know.

### Loboris Display Module
https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/display
LoBo has a really good display module built in which supports the ST7899 on the TTGO T-Display module.

# Loads image from particle pi server (latest image from eia365 on intsagram)
# And displays on ST7899 screen
# Loboris Display reference at https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/display
