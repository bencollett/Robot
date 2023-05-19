
import time
from machine import Pin, I2C
import def_us as us
import def_pdcontrol as pdc
import def_motorcontrol as mc
from oled import SSD1306_I2C as ss

print('hello world')

"""define global variables and arrays"""

state = 'corridor'
i2c = I2C(0, sda=Pin(12), scl=Pin(13))
rv = [0, 0]  # right us array
lv = [0, 0]  # left us array
dta = [0, 1]  # code run time array

while state == 'corridor':
    dt = time.time()
    dta.append(dt)
    servo = us.Servo()  # initialize Class Servo
    servo.sweep(direction='right', anglel=35, angler=155)  # sweep right
    rv1 = servo.rv
    servo.sweep(direction='left', anglel=25, angler=170)  # sweep left
    lv1 = servo.lv
    servo.sweep(direction='right', anglel=45, angler=130)  # sweep right
    rv2 = servo.rv
    rv.append((rv1 + rv2) / 2)
    servo.sweep(direction='left', anglel=45, angler=130)  # sweep left
    lv2 = servo.lv
    lv.append((lv1 + lv2) / 2)

    """us pd code"""
    control = pdc.PDControl()
    uspd = control.us_pdcontrol(lv[len(lv)-1], lv[len(lv)-2], rv[len(rv)-1], rv[len(rv)-2], dta[len(dta)-1], dta[len(dta)-2])
    if - 28 < uspd < 28:
        pd = int(uspd)
    elif - 28 > uspd:
        pd = - 28
    else:
        pd = 28

    """Activate motor control"""
    if (lv[len(lv) - 1]) < 40 or (rv[len(rv) - 1]) < 40:
        vel = 50
        slp = 0.1
        cv = 1
    elif (lv[len(lv) - 1]) < 70 or (rv[len(rv) - 1]) < 70:
        vel = 50
        slp = 0.18
        cv = 1
    elif (lv[len(lv) - 1]) < 100 or (rv[len(rv) - 1]) < 100:
        vel = 50
        slp = 0.3
        cv = 1
    else:
        vel = 50
        slp = 0.45
        cv = 1
    mcontrol = mc.Motorcontrol(cv)
    mcontrol.set_motor1(pd, vel, slp)

    """Activate Oled and print desired values"""
    oled = ss(128, 64, i2c)
    text1 = "pd = {}".format(pd)
    text2 = "r_s = {}".format(rv[len(rv) - 1])
    text3 = "l_s = {}".format(lv[len(lv) - 1])

    oled.text(str(text1), 0, 0)
    oled.text(str(text2), 0, 10)
    oled.text(str(text3), 0, 20)
    oled.show()


