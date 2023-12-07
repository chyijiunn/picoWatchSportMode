# 製作 python 程式間連結，使得螢幕中點移到右邊後，進入碼表程式
from machine import Pin, SPI
from fonts import vga2_16x32 as font
import gc9a01py as gc9a01
import random ,utime ,RP

spi = SPI(1, baudrate=62500000, sck=Pin(10), mosi=Pin(11))
LCD = gc9a01.GC9A01(spi,dc=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),reset=Pin(12, Pin.OUT),backlight=Pin(25, Pin.OUT),rotation=0)
color = gc9a01.color565

LCD.fill(color(0,0,0))
ori_x , ori_y = 120 ,120 
while True:
    xyz = RP.QMI8658().Read_XYZ()
    
    # 這邊和 04_moveDot_Acc 一樣，僅加權不同
    # 往右傾斜，xyz[1]增加，需加在螢幕 x 座標，所以為 ori_x + y_shift
    # 往上傾斜，xyz[0]增加，需[減]螢幕 y 座標，所以為 ori_y - x_shift
    LCD.pixel(ori_x+int(5*xyz[1]),ori_y-int(5*xyz[0]),color(255,255,255))
    ori_x = ori_x+int(5*xyz[1])
    ori_y = ori_y - int(5*xyz[0])
    
    if ori_x > 240:
        from stoptime import *
        stoptime_main() # 進入碼表程式
                        # 碼表主程式寫成一個函式，
                        # 設立 break 條件，若滿足 break 條件則跳出 while 迴圈
        break           # 原始 if 條件式也需要 break，否則會再度進入碼表程式
