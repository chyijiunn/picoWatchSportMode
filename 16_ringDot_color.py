import time , RP, math

LCD = RP.LCD_1inch28()
qmi8658 = RP.QMI8658()
LCD.set_bl_pwm(15535)
cx , cy =120 ,120 #center of watch
NUM = 0
TARGET = 1000#每天要走幾步
                
def runDotRing(reach , spinLen , color):
    r = 12
    #now = list(time.localtime())
    x = int(spinLen*math.sin(math.radians(reach*360)))
    y = int(spinLen*math.cos(math.radians(reach*360)))
    for i in range(-r,r,1):
        for j in range(-r,r,1):
            if i*i + j*j <= r*r:
                LCD.pixel(cx+x+i,cy-y+j,color)

def color(R,G,B): #  RGB888 to RGB565
    return (((G&0b00011100)<<3) +((B&0b11111000)>>3)<<8) + (R&0b11111000)+((G&0b11100000)>>5)

while 1:
    
    xyz=qmi8658.Read_XYZ()
    N1 = xyz[5]
    time.sleep(0.1)
    xyz=qmi8658.Read_XYZ()
    N2 = xyz[5]
    if N1*N2 < 0:NUM=NUM+1
    reach = float(NUM/TARGET)
    runDotRing(reach,110,color(NUM,180,NUM))#點繞行
    LCD.text(str(reach*100)+'%',110,120,color(NUM,180,NUM))
    LCD.show()
    LCD.fill_rect(110,120,50,10,color(255,255,255))

