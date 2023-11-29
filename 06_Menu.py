from machine import Pin, SPI
from fonts.romfonts import vga2_16x32 as font
import gc9a01py as gc9a01
import random ,utime ,RP

spi = SPI(1, baudrate=62500000, sck=Pin(10), mosi=Pin(11))
LCD = gc9a01.GC9A01(spi,dc=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),reset=Pin(12, Pin.OUT),backlight=Pin(25, Pin.OUT),rotation=0)
color = gc9a01.color565

LCD.fill(color(0,0,0))
ori_x , ori_y = 120 ,120 
while True:
    xyz = RP.QMI8658().Read_XYZ()
    LCD.pixel(ori_x+int(5*xyz[1]),ori_y-int(5*xyz[0]),color(255,255,255))
    ori_x = ori_x+int(5*xyz[1])
    ori_y = ori_y - int(5*xyz[0])
    
    if ori_x > 240:
        from stoptime import *
        stoptime_main()
        break
