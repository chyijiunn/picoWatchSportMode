import time , RP, math

LCD = RP.LCD_1inch28()
qmi8658 = RP.QMI8658()
LCD.set_bl_pwm(30000)

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

def color(R,G,B): #  RGB888 to RGB565
    return (((G&0b00011100)<<3) +((B&0b11111000)>>3)<<8) + (R&0b11111000)+((G&0b11100000)>>5)

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
    
    runDotRing(12,walkreach,110,color(walknum,180,walknum))#點繞行
    runDotRing(12,runreach,88,color(runnum,180,180))
    
    LCD.text(str(int(walkreach*100))+'%'+str(walknum),110,120,color(int(walkreach*128),180,int(walkreach*128)))
    LCD.text(str(int(runreach*100))+'%'+str(runnum),110,100,color(int(runreach*128),180,180))
    
    LCD.show()
    LCD.fill_rect(110,100,50,30,LCD.white)

