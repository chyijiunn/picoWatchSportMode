#利用六軸的加速度方向 xyz [0]~[2] 來控制螢幕上的點
from RP import *

LCD = LCD_1inch28()
LCD.set_bl_pwm(30000)
qmi8658=QMI8658()
Vbat= ADC(Pin(Vbat_Pin))

r = 5
ori_x = 120
ori_y = 120
while True:
    LCD.fill(LCD.cyan)
    xyz=qmi8658.Read_XYZ()
    x_shift = int(xyz[0]*20)#讀取X軸加速度值，若替換為角加速度[3]呢？
    y_shift = int(xyz[1]*20)
    
    for i in range(-r,r,1):
        for j in range(-r,r,1):
            if i*i + j*j <= r*r:
                #往右傾斜，xyz[1]增加，需加在螢幕 x 座標，所以為 ori_x + y_shift
                #往上傾斜，xyz[0]增加，需[減]螢幕 y 座標，所以為 ori_y - x_shift
                LCD.pixel(ori_x+y_shift + j ,ori_y-x_shift + i,LCD.white)
                
    ori_x = ori_x + y_shift
    ori_y = ori_y - x_shift
    
    if   ori_x >= 150:ori_x=150
    if   ori_x <= 90:ori_x=90
    if   ori_y >= 200:ori_y=200
    if   ori_y <= 60:ori_y=60
    
    LCD.text("x",60,25,LCD.white)
    LCD.text(str(round(xyz[0],2)),60,40,LCD.white)
    LCD.text("y",180,25,LCD.white)
    LCD.text(str(round(xyz[1],2)),150,40,LCD.white)
    LCD.show()