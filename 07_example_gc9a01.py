from machine import Pin, SPI
from fonts import vga2_16x32 as font
import time
import gc9a01py as gc9a01

spi = SPI(1, baudrate=62500000, sck=Pin(10), mosi=Pin(11))
LCD = gc9a01.GC9A01(spi,dc=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),reset=Pin(12, Pin.OUT),backlight=Pin(25, Pin.OUT),rotation=0)
color = gc9a01.color565

LCD.fill(color(0,0,0))
LCD.vline(120,20,50,color(200,45,100))
LCD.line(120,20,50,50,color(200,45,100))
LCD._text16(font,'Trunking_1',40,80)
LCD.text(font, 'Trunking_2', 40, 120)
for line in range(40, 280, 1):
            LCD.vscsad(line)
            time.sleep(0.01)


