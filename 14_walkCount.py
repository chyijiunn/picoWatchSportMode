#寫一個計步器
from RP import *
import utime

LCD = LCD_1inch28()
LCD.set_bl_pwm(30000)
qmi8658=QMI8658()
NUM = 0

def circle(cx,cy,rr,color=LCD.white):
    for i in range(-rr,rr,1):
        for j in range(-rr,rr,1):
            if i*i + j*j <= rr*rr:
                LCD.pixel(cx+i,cy-j,color)                
def COUNT(NUM):
    LCD.fill(LCD.cyan)
    LCD.text(str(NUM),110,200,LCD.white)

while True:
    xyz=qmi8658.Read_XYZ()
    N1 = xyz[5]
    utime.sleep(0.1)
    xyz=qmi8658.Read_XYZ()
    N2 = xyz[5]
    if N1*N2 < 0:
        NUM=NUM+1
        COUNT(NUM)
        circle(120,120,NUM)
    LCD.show()