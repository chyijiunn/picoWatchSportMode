import time , RP, math

LCD = RP.LCD_1inch28()
qmi8658 = RP.QMI8658()
LCD.set_bl_pwm(15535)
cx , cy =120 ,120 #center of watch
NUM = 0
TARGET = 100
                
def runDotRing(tic , spinLen , color):
    r = 10
    #now = list(time.localtime())
    x = int(spinLen*math.sin(math.radians(NUM/TARGET*360)))
    y = int(spinLen*math.cos(math.radians(NUM/TARGET*360)))
    for i in range(-r,r,1):
        for j in range(-r,r,1):
            if i*i + j*j <= r*r:
                LCD.pixel(cx+x+i,cy-y+j,color)

while 1:
    xyz=qmi8658.Read_XYZ()
    N1 = xyz[5]
    time.sleep(0.1)
    xyz=qmi8658.Read_XYZ()
    N2 = xyz[5]
    if N1*N2 < 0:NUM=NUM+1
    runDotRing(NUM,110,LCD.red)#紅點繞行秒針
    LCD.show()

