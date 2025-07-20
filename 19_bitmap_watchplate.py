from machine import Pin, SPI
from fonts import vga2_16x16 as font
import time , watch #記得引入 轉檔後名稱.py
import gc9a01py as gc9a01

spi = SPI(1, baudrate=62500000, sck=Pin(10), mosi=Pin(11))
LCD = gc9a01.GC9A01(spi,dc=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),reset=Pin(12, Pin.OUT),backlight=Pin(25, Pin.OUT),rotation=0)
color = gc9a01.color565

LCD.fill(color(0,0,0))
# LCD.bitmap(檔名.py,起始 x ,起始 y)
LCD.bitmap(watch,0,0)