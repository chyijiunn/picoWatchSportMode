from machine import Pin, SPI
from fonts.romfonts import vga2_16x32 as font
import gc9a01py as gc9a01
import random ,utime , RP

spi = SPI(1, baudrate=62500000, sck=Pin(10), mosi=Pin(11))
LCD = gc9a01.GC9A01(spi,dc=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),reset=Pin(12, Pin.OUT),backlight=Pin(25, Pin.OUT),rotation=0)
color = gc9a01.color565

N1 = utime.ticks_ms()#Start 時刻
digitalxstart = 60
digitalystart = 100
R,G,B = (random.getrandbits(8),random.getrandbits(8),random.getrandbits(8))
comColor = (256-R,256-G,256-B)
BG = color(R,G,B)
FC = color(comColor)
LCD.fill(BG)
data = open('Record','a')

while True:
    xyz0 = RP.QMI8658().Read_XYZ()#Data_ini
    N2 = utime.ticks_ms()-N1#End 時刻
    cS = int(N2//10)#百分秒
    S = int(N2 //1000)#秒
    M =int(S//60)#分
    H =int(M//60)#時
    now = str(H)+':'+str(M%60)+':'+str(S%60)+'.'+str(cS%100)
    LCD.text(font,now,digitalxstart,digitalystart,FC,BG)
    utime.sleep(0.05)
    xyz1 = RP.QMI8658().Read_XYZ()#Data_Final
    
    #print(now,',',xyz1[3]-xyz0[3],',',xyz1[4]-xyz0[4],',',xyz1[5]-xyz0[5])
    if xyz1[5]*xyz0[5]<0:
        data.write(str(now)+','+str(round(100*(xyz1[3]-xyz0[3]),2))+','+str(round(100*(xyz1[4]-xyz0[4]),2))+','+str(round(100*(xyz1[5]-xyz0[5]),2))+'\n')
