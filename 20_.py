from machine import Pin, SPI
import time , batman , RP, math#記得引入 batman
import gc9a01py as gc9a01

spi = SPI(1, baudrate=62500000, sck=Pin(10), mosi=Pin(11))
LCD = gc9a01.GC9A01(spi,dc=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),reset=Pin(12, Pin.OUT),backlight=Pin(25, Pin.OUT),rotation=0)
color = gc9a01.color565

LCD.fill(color(255,225,0))
LCD.bitmap(batman,90,90)

LCD = RP.LCD_1inch28()
qmi8658 = RP.QMI8658()
LCD.set_bl_pwm(5535)

cx , cy =120 ,120 #center of watch
walknum = 0
walkTARGET = 100 # 每天要走幾步

runnum = 0
runTARGET = 100 # 每天要跑幾步

threhold = 300
                
def runDotRing(r , walkreach , spinLen , color):
    x = int(spinLen*math.sin(math.radians(walkreach*360)))
    y = int(spinLen*math.cos(math.radians(walkreach*360)))
    for i in range(-r,r,1):
        for j in range(-r,r,1):
            if i*i + j*j <= r*r:
                LCD.pixel(cx+x+i,cy-y+j,color)

while 1:
    xyz=qmi8658.Read_XYZ()
    N1 = xyz[5]
    time.sleep(0.05)
    xyz=qmi8658.Read_XYZ()
    N2 = xyz[5]
    if N1*N2 < 0:
        if (N1>10 and N1<threhold) or (N2>10 and N2<threhold):
            walknum = walknum + 1
        elif (N1 or N2) > threhold or (N1 or N2)< -threhold :
            runnum = runnum + 1
            
    walkreach = walknum/walkTARGET
    runreach = runnum/runTARGET

    runDotRing(12,walkreach,110,color(walknum,180,walknum))
    runDotRing(12,runreach,88,color(runnum,180,180))
    LCD.show()


