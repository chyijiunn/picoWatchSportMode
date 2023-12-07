from machine import Pin, SPI
from fonts import vga2_bold_16x32 as font
import gc9a01py as gc9a01
import random ,utime ,RP

spi = SPI(1, baudrate=62500000, sck=Pin(10), mosi=Pin(11))
LCD = gc9a01.GC9A01(spi,dc=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),reset=Pin(12, Pin.OUT),backlight=Pin(25, Pin.OUT),rotation=0)
color = gc9a01.color565


N1 = utime.ticks_ms()# 讀取 utime.ticks_ms() 存為 N1
digitalxstart = 60
digitalystart = 100
R,G,B = (random.getrandbits(8),random.getrandbits(8),random.getrandbits(8))
comColor = (256-R,256-G,256-B)
#設定前景色與背景色
BG = color(R,G,B)
FC = color(comColor)
LCD.fill(BG)

while True:
    N2 = utime.ticks_ms()-N1# 讀取 utime.ticks_ms() 減去 N1 存為 N2
    cS = int(N2//10)#百分秒，捨棄千分位，使用 // 10 得到商，轉為整數
    S = int(N2 //1000)#秒，取個位，使用 // 1000 得到商，轉為整數
    M =int(S//60)#分，根據累積的秒 // 60 得到商，轉整數
    H =int(M//60)#時，根據累積的分 // 60 得到商，轉整數
    
    # 將上述資料轉字串外
    # 分鐘顯示為餘數資料，以 % 計算，秒數亦同，
    # 百分秒取 %100 的餘數
    now = str(H)+':'+str(M%60)+':'+str(S%60)+'.'+str(cS%100)
    # 顯示於 LCD.text(字型,字串內容,起始x , 起始y,前景色,背景色)
    LCD.text(font,now,digitalxstart,digitalystart,FC,BG)

    
