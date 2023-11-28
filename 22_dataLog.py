from RP import *
import utime

LCD = LCD_1inch28()
LCD.set_bl_pwm(30000)#亮度~65535
qmi8658=QMI8658()
Vbat= ADC(Pin(Vbat_Pin))

ori_x = 120
ori_y = 120
N1 = utime.ticks_ms()

def circle(cx,cy,rr,color=LCD.white):
    for i in range(-rr,rr,1):
        for j in range(-rr,rr,1):
            if i*i + j*j <= rr*rr:
                LCD.pixel(cx+i,cy-j,color)
def BG():
    LCD.fill(LCD.cyan)
    circle(160,120,20)
    circle(80,120,20)
    LCD.text('START',140,80,LCD.white)
    LCD.text('STOP',60,80,LCD.white)
while True:
    #BG()
    xyz=qmi8658.Read_XYZ()
    for i in range(3,6,1):
        print(round(xyz[i],2),'',end ='')
    print()
    utime.sleep(0.4)
    
    data = open('training','a')
    data.write(str(xyz[0])+','+str(xyz[1])+','+str(xyz[2])+'\n')
    data.close()
    
    #datatab.net使用
'''
    circle(ori_x+x_shift,ori_y-y_shift,20,LCD.yellow)
    ori_x = ori_x - x_shift
    ori_y = ori_y - y_shift
    if  ori_x >= 160:
        ori_x = 160
        N1 = utime.ticks_ms()
        LCD.text(str(N1/1000),110,25,LCD.white)
        LCD.show()
    if ori_x <= 80:
        ori_x = 80
        N2 = utime.ticks_ms()
        stop = (N2-N1)/1000
        LCD.text(str(stop),110,25,LCD.white)
        LCD.show()
        break
    if   ori_y >= 160:ori_y=160
    if   ori_y <= 80:ori_y=80

    LCD.show()
    '''