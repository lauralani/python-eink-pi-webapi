#!/usr/bin/python
# -*- coding:utf-8 -*-

async def clear_display():

    import sys
    import os
    resdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'res')

    if os.path.exists(resdir):
        sys.path.append(resdir)
    import logging
    from res import epd2in13_V2

    try:
        epd = epd2in13_V2.EPD()
        logging.debug("init and Clear")
        epd.init(epd.FULL_UPDATE)
        epd.Clear(0xFF)
        
        logging.debug("Goto Sleep...")
        epd.sleep()
        return "ok"
            
    except Exception as e:
        logging.error(e)
        return "error"


async def set_display_text( text, fontsize ):

    import sys
    import os
    resdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'res')

    if os.path.exists(resdir):
        sys.path.append(resdir)

    import logging
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

        logging.debug(os.path.join(resdir, 'Font.ttc'))

        # Drawing on the image
        # font15 = ImageFont.truetype(os.path.join(resdir, 'Font.ttc'), 15)
        # font24 = ImageFont.truetype(os.path.join(resdir, 'Font.ttc'), 24)
        # font32 = ImageFont.truetype(os.path.join(resdir, 'Font.ttc'), 32)

        font = ImageFont.truetype(os.path.join(resdir, 'Font.ttc'), fontsize)
        
        logging.debug("drawing text")
        image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
        draw = ImageDraw.Draw(image)
        
        #draw.rectangle([(0,0),(50,50)],outline = 0)
        #draw.rectangle([(55,0),(100,50)],fill = 0)
        #draw.line([(0,0),(50,50)], fill = 0,width = 1)
        #draw.line([(0,50),(50,0)], fill = 0,width = 1)
        #draw.chord((10, 60, 50, 100), 0, 360, fill = 0)
        #draw.ellipse((55, 60, 95, 100), outline = 0)
        #draw.pieslice((55, 60, 95, 100), 90, 180, outline = 0)
        #draw.pieslice((55, 60, 95, 100), 270, 360, fill = 0)
        #draw.polygon([(110,0),(110,50),(150,25)],outline = 0)
        #draw.polygon([(190,0),(190,50),(150,25)],fill = 0)
        #draw.text((120, 60), 'e-Paper demo', font = font15, fill = 0)
        #draw.text((0, 0), 'P E N I S', font = font32, fill = 0)
        #draw.text((110, 90), u'微雪电子', font = font24, fill = 0)

        draw.text((0, 0), text, font = font, fill = 0)

        epd.display(epd.getbuffer(image))
        time.sleep(2)
        
        # read bmp file 
        # logging.info("2.read bmp file...")
        # image = Image.open(os.path.join(resdir, '2in13.bmp'))
        # epd.display(epd.getbuffer(image))
        # time.sleep(2)
        # 
        # # read bmp file on window
        # logging.info("3.read bmp file on window...")
        # # epd.Clear(0xFF)
        # image1 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
        # bmp = Image.open(os.path.join(resdir, '100x100.bmp'))
        # image1.paste(bmp, (2,2))    
        # epd.display(epd.getbuffer(image1))
        # time.sleep(2)
        
        # # partial update
        # logging.info("4.show time...")
        # time_image = Image.new('1', (epd.height, epd.width), 255)
        # time_draw = ImageDraw.Draw(time_image)
        # 
        # epd.init(epd.FULL_UPDATE)
        # epd.displayPartBaseImage(epd.getbuffer(time_image))
        
        #epd.init(epd.PART_UPDATE)
        #num = 0
        #while (True):
        #    time_draw.rectangle((120, 80, 220, 105), fill = 255)
        #    time_draw.text((120, 80), time.strftime('%H:%M:%S'), font = font24, fill = 0)
        #    epd.displayPartial(epd.getbuffer(time_image))
        #    num = num + 1
        #    if(num == 10):
        #        break
        ## epd.Clear(0xFF)
        
        
        
        
        #logging.info("Clear...")
        #epd.init(epd.FULL_UPDATE)
        #epd.Clear(0xFF)
        
        logging.info("Goto Sleep...")
        epd.sleep()
        return "ok"
            
    except IOError as e:
        logging.error(e)
        return "ioerror"
        
    except KeyboardInterrupt:    
        logging.error("ctrl + c:")
        epd2in13_V2.epdconfig.module_exit()
        return "error"
