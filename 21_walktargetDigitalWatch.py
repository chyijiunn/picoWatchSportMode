# 結合走路資料在外圈
from machine import Pin, SPI
from fonts import vga2_16x32 as font
import time  ,math,RP,bmp#記得引入 轉檔後 檔名
import gc9a01py as gc9a01

spi = SPI(1, baudrate=62500000, sck=Pin(10), mosi=Pin(11))
LCD = gc9a01.GC9A01(spi,dc=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),reset=Pin(12, Pin.OUT),backlight=Pin(25, Pin.OUT),rotation=0)
color = gc9a01.color565
qmi8658 = RP.QMI8658()

LCD.fill(color(255,225,0))
LCD.bitmap(bmp,90,90)

cx , cy =120 ,120 #center of watch
NUM = 0
TARGET = 100#每天要走幾步

def runDotRing(reach , spinLen , color):
    r = 12
    x = int(spinLen*math.sin(math.radians(reach*360)))
    y = int(spinLen*math.cos(math.radians(reach*360)))
    for i in range(-r,r,1):
        for j in range(-r,r,1):
            if i*i + j*j <= r*r:
                LCD.pixel(cx+x+i,cy-y+j,color)
while 1:
    xyz=qmi8658.Read_XYZ()
    N1 = xyz[5]
    now = list(time.gmtime())
    LCD._text16(font,'{0:0>2}:{1:0>2}:{2:0>2}'.format(now[3],now[4],now[5]),60,160,color(0,0,0),color(255,225,0))
    xyz=qmi8658.Read_XYZ()
    N2 = xyz[5]
    if N1*N2 < 0:
        NUM = NUM + 1
    reach = NUM/TARGET
    colorfactor = int(255*(1-reach))
    runDotRing(reach,110,color(colorfactor,200,colorfactor))
