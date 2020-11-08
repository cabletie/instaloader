import machine, display, urequests, lib.shutil as shutil, os, sys, utime
# Loads image from particle pi server (latest image from eia365 on intsagram)
# And displays on ST7899 screen
# Loboris Display reference at https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/display
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Boganville', 'potsticker')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

# initialize the display
tft=display.TFT()
tft.init(tft.ST7789, rst_pin=23, backl_pin=4, miso=0, mosi=19, clk=18, cs=5, dc=16, width=235, height=340, backl_on=1, rot=tft.LANDSCAPE)

# invert colors
tft.tft_writecmd(0x21)

# set window size
tft.setwin(40, 52, 279, 186)
tft.clear()
tft.text(tft.CENTER, tft.CENTER, 'Connecting...')
# Start networking
do_connect()

while True:
    tft.clear()
    tft.text(tft.CENTER, tft.CENTER, 'Loading image...')

    ## Set up the image URL and filename
    image_url = "http://particlepi.lan/eia365/latest_135.jpg"
    filename = image_url.split("/")[-1]
    # filename = "latest.jpg"

    # Open the url image, set stream to True, this will return the stream content.
    r = urequests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        # r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        r.close()

        print('Image sucessfully Downloaded: ',filename)
        # Display the image
    else:
        print('Image Couldn\'t be retreived')

    tft.image(tft.CENTER,tft.CENTER,filename)
    tft.font(tft.FONT_Minya ,rotate=90)
    tft.text(tft.CENTER,tft.CENTER,'(c) eia365')

    # Loop after 15 minutes to reload
    utime.sleep(900) # 15 minutes
