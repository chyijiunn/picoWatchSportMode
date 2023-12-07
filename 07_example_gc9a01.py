# 為了有不同字型，上傳資料夾 lib 內，包含 gc9a01py 和 fonts 字型資料夾
# gc9a01py顯示完文字即可顯示，不需要再 LCD.show()
# 缺點是若要畫圓的 pixel 會一個點一個點畫完就 show ，時間比較慢
# 為了百分秒錶呈現方便性，引用 gc9a01py 較為便捷。以下為 gc9a01py 使用範例：
from machine import Pin, SPI
from fonts import vga2_16x32 as fontL
from fonts import vga2_8x16 as fontS
import time
import gc9a01py as gc9a01

spi = SPI(1, baudrate=62500000, sck=Pin(10), mosi=Pin(11))
LCD = gc9a01.GC9A01(spi,dc=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),reset=Pin(12, Pin.OUT),backlight=Pin(25, Pin.OUT),rotation=0)
color = gc9a01.color565

LCD.fill(color(0,0,0))
LCD.vline(120,20,50,color(200,45,100))#另有hline
LCD.line(120,20,50,50,color(200,45,100))
LCD._text16(fontL,'Trunking_1',40,80)
LCD.text(fontL, 'Trunking_2', 40, 120)#隱藏前景色、背景色引數
#這裡開始為上拉畫面
for line in range(40, 280, 1):
            LCD.vscsad(line)
            time.sleep(0.01)