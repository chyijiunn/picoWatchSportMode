# 練習六軸的資料，看數值變化與方向的關聯性，
from RP import *

LCD = LCD_1inch28()
LCD.set_bl_pwm(30000)#亮度~65535
qmi8658=QMI8658()

while True:
    xyz=qmi8658.Read_XYZ()
    print(xyz[5])#xyz[] from 0~6