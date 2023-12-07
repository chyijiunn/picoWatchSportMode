# 製作背景選單，使點可以選擇左邊或右邊的圈
from RP import *
LCD = LCD_1inch28()
LCD.set_bl_pwm(30000)
qmi8658=QMI8658()
Vbat= ADC(Pin(Vbat_Pin))

r = 10
ori_x = 120
ori_y = 120

def circle(cx,cy,r=25):
    for i in range(-r,r,1):
        for j in range(-r,r,1):
            if i*i + j*j <= r*r:
                LCD.pixel(cx+i+r,cy+j-r,LCD.white)
            
def BG():
    LCD.fill(LCD.cyan)
    
while True:
    BG()
    circle(140,150)
    circle(60,150)
    xyz=qmi8658.Read_XYZ()
    x_shift = int(xyz[3]/10)
    y_shift = int(xyz[4])
    for i in range(-r,r,1):
        for j in range(-r,r,1):
            if i*i + j*j <= r*r:
                LCD.pixel(ori_x+i-x_shift,ori_y+j-y_shift,LCD.yellow)
    ori_x = ori_x - x_shift
    #ori_y = ori_y - y_shift
    if   ori_x >= 150:ori_x=150
    if   ori_x <= 90:ori_x=90
    if   ori_y >= 200:ori_y=200
    if   ori_y <= 60:ori_y=60

    LCD.show()