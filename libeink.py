#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging

async def clear_display():

    resdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'res')

    if os.path.exists(resdir):
        sys.path.append(resdir)
    from res import epd2in13_V2

    try:
        epd = epd2in13_V2.EPD()
        logging.debug("init and Clear")
        epd.init(epd.FULL_UPDATE)
        epd.Clear(0xFF)
        
        logging.debug("Goto Sleep...")
        epd.sleep()
        return "success"
            
    except Exception as e:
        logging.error(e)
        return "error"


async def set_display_text( text, fontsize ):

    resdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'res')

    if os.path.exists(resdir):
        sys.path.append(resdir)

    from res import epd2in13_V2
    import time
    from PIL import Image,ImageDraw,ImageFont
    import traceback

    try:
        logging.debug("epd2in13_V2 Demo")
        
        epd = epd2in13_V2.EPD()
        logging.debug("init and Clear")
        epd.init(epd.FULL_UPDATE)
        epd.Clear(0xFF)

        font = ImageFont.truetype(os.path.join(resdir, 'CascadiaMono.ttf'), fontsize)
        
        logging.debug("drawing text")
        image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
        draw = ImageDraw.Draw(image)

        draw.text((0, 0), text, font = font, fill = 0)


        image.save("./display.png", "PNG")
        epd.display(epd.getbuffer(image))
        time.sleep(2)

        logging.debug("Goto Sleep...")
        epd.sleep()
        return "success"
            
    except IOError as e:
        logging.error(e)
        return "ioerror"
        
    except KeyboardInterrupt:    
        logging.error("ctrl + c:")
        epd2in13_V2.epdconfig.module_exit()
        return "error"
