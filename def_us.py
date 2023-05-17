
class Servo(object):

    def __init__(self):
        self.s_value = ()
        self.rv = ()
        self.lv = ()
        self.straight = self.s_value
        self.right = self.rv
        self.left = self.lv
        self.state = ()

    def setServoAngle(self, angle):
        from machine import PWM, Pin
        pwm = PWM(Pin(15))
        pwm.freq(50)

        position = int(8000 * (angle / 180) + 1000)
        pwm.duty_u16(position)

    def sweep(self, direction, angler, anglel):
        import ultrasonic
        from time import sleep
        TRIG = 3
        ECHO = 2
        us = ultrasonic.sonic(TRIG, ECHO)
        dist = us.distance_mm()
        angle_r = angler
        angle_l = anglel

        if direction == 'right':
            for pos in range(0, 180, 40):       # 0 (range para.), 180 (range para.), 20 (speed of sweep)
                self.setServoAngle(angle_r)
                sleep(0.04)
                rv = dist       # add ultrasonic distance reading to s_value array in main
                if rv > 200:
                    self.rv = 200
                    self.state = 'line' #todo
                else:
                    self.rv = rv
        elif direction == 'left':
            for pos in range(0, 180, 40):
                self.setServoAngle(angle_l)
                sleep(0.04)
                lv = dist
                if lv > 200:
                    self.lv = 200
                    self.state = 'line'
                else:
                    self.lv = lv
        # elif direction == 'straight':
        #     for pos in range(0, 180, 20):
        #         self.setServoAngle(25)
        #         sleep(0.05)
        #         s_value = dist
        #         if s_value > 200:
        #             self.s_value = 200
        #         else:
        #             self.s_value = s_value










