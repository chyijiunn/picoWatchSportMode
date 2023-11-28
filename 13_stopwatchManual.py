from fonts.romfonts import vga2_16x32 as font
import random ,utime, gc9a01py ,RP,_thread

LCD = gc9a01py.GC9A01()
color = gc9a01py.color565
qmi8658=RP.QMI8658()

N1 = utime.ticks_ms()#Start 時刻
digitalxstart = 60
digitalystart = 100
R,G,B = (random.getrandbits(8),random.getrandbits(8),random.getrandbits(8))
comColor = (256-R,256-G,256-B)
BG = color(R,G,B)
FC = color(comColor)
LCD.fill(BG)

ori_x = 120
ori_y = 120

def circle(cx,cy,rr=10,color=FC):
    for i in range(-rr,rr,1):
        for j in range(-rr,rr,1):
            if i*i + j*j <= rr*rr:
                LCD.pixel(cx+i,cy-j,color)

def dot():
    global ori_x , ori_y
    LCD.fill(BG)
    xyz=qmi8658.Read_XYZ()
    x_shift = int(xyz[3]//10)
    y_shift = int(xyz[4]//10)
    circle(ori_x+x_shift,ori_y-y_shift)
    ori_x = ori_x - x_shift
    ori_y = ori_y - y_shift

def stopwatch():
    while True:
        N2 = utime.ticks_ms()-N1#End 時刻
        cS = int(N2//10)#百分秒
        S = int(N2 //1000)#秒
        M =int(S//60)#分
        H =int(M//60)#時
        now = str(H)+':'+str(M%60)+':'+str(S%60)+'.'+str(cS%100)
        LCD.text(font,now,digitalxstart,digitalystart,FC,BG)
    
_thread.start_new_thread(stopwatch, ())
while True:
    dot()
