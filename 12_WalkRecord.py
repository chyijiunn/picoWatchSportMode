# 讀取走路的角加速度差異值，並記錄
# 記錄
#     1.utime.ticks_ms() 時間差
#     2.同時呈現碼錶面資料
#     3.角加速度 - 利用手部晃動時，若加速度發生正負變換，就記錄

from machine import Pin, SPI
from fonts import vga2_16x32 as font
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
data = open('record_fix.csv','a')

while True:
    xyz0 = RP.QMI8658().Read_XYZ()#Data_ini
    N2 = utime.ticks_ms()-N1#End 時刻
    cS = int(N2//10)#百分秒
    S = int(N2 //1000)#秒
    M =int(S//60)#分
    H =int(M//60)#時
    now = str(H)+':'+str(M%60)+':'+str(S%60)+'.'+str(cS%100)
    LCD.text(font,now,digitalxstart,digitalystart,FC,BG)
    xyz1 = RP.QMI8658().Read_XYZ()#Data_Final
    
    #print(now,',',xyz1[3]-xyz0[3],',',xyz1[4]-xyz0[4],',',xyz1[5]-xyz0[5])

    if xyz1[5]*xyz0[5]<0:#為了看出區別，放大scale
        data.write(str(now)+','+str(round(1000*xyz1[0],3)) +','+str(1000*round(xyz1[1],3))+','+str(1000*round(xyz1[2],3))+','+str(round(100*(xyz1[3]-xyz0[3]),2))+','+str(round(100*(xyz1[4]-xyz0[4]),2))+','+str(round(100*(xyz1[5]-xyz0[5]),2))+'\n')
        #data.write(str(now)+','+str(round(xyz1[3]-xyz0[3],2))+','+str(round(xyz1[4]-xyz0[4],2))+','+str(round(xyz1[5]-xyz0[5],2))+'\n')