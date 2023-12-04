from machine import Pin, SPI
from fonts import vga2_16x32 as font
import gc9a01py as gc9a01
import random ,utime ,RP
spi = SPI(1, baudrate=62500000, sck=Pin(10), mosi=Pin(11))
LCD = gc9a01.GC9A01(spi,dc=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),reset=Pin(12, Pin.OUT),backlight=Pin(25, Pin.OUT),rotation=0)
color = gc9a01.color565
ori_x , ori_y = 120 ,120

def stoptime_main():
    N1 = utime.ticks_ms()#Start 時刻
    digitalxstart = 60
    digitalystart = 100
    R,G,B = (random.getrandbits(8),random.getrandbits(8),random.getrandbits(8))
    comColor = (256-R,256-G,256-B)
    BG = color(R,G,B)
    FC = color(comColor)
    LCD.fill(BG)

    while True:
        xyz0 = RP.QMI8658().Read_XYZ()#Data_ini
        
        N2 = utime.ticks_ms()-N1#End 時刻
        cS = int(N2//10)#百分秒
        S = int(N2 //1000)#秒
        M =int(S//60)#分
        H =int(M//60)#時
        now = str(H)+':'+str(M%60)+':'+str(S%60)+'.'+str(cS%100)
        LCD.text(font,now,digitalxstart,digitalystart,FC,BG)
        
        #xyz1 = RP.QMI8658().Read_XYZ()#Data_Final
        
        if xyz0[1] < -0.95 :break#y軸近垂直於地面，左手朝上
        
    LCD.text(font,now,digitalxstart,digitalystart,FC,BG)
    LCD.text(font,'TimeUP',digitalxstart+10,digitalystart+40,FC,BG)
