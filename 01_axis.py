from RP import *

LCD = LCD_1inch28()
LCD.set_bl_pwm(30000)#亮度~65535
qmi8658=QMI8658()

while True:
    xyz=qmi8658.Read_XYZ()
    print(xyz[5])