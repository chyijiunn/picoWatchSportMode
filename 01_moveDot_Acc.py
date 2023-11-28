from RP import *

LCD = LCD_1inch28()
LCD.set_bl_pwm(30000)#亮度~65535
qmi8658=QMI8658()
Vbat= ADC(Pin(Vbat_Pin))

r = 10
ori_x = 120
ori_y = 120
while True:
    LCD.fill(LCD.cyan)
    xyz=qmi8658.Read_XYZ()
    x_shift = int(xyz[0]*30)#讀取X軸加速度值，若替換為角加速度[3]呢？
    y_shift = int(xyz[1]*30)
    
    for i in range(-r,r,1):
        for j in range(-r,r,1):
            if i*i + j*j <= r*r:
                LCD.pixel(ori_x+j+y_shift,ori_y+i-x_shift,LCD.white)
                
    ori_x = ori_x - x_shift
    ori_y = ori_y - y_shift
    
    if   ori_x >= 150:ori_x=150
    if   ori_x <= 90:ori_x=90
    if   ori_y >= 200:ori_y=200
    if   ori_y <= 60:ori_y=60
    
    LCD.text("x",60,25,LCD.white)
    LCD.text("{:+3.2f}".format(xyz[0]),60,40,LCD.white)
    LCD.text("y",180,25,LCD.white)
    LCD.text("{:+3.2f}".format(xyz[1]),150,40,LCD.white)
    LCD.show()



