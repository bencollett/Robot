class Motorcontrol:

    def __init__(self, control_vertical):
        self.cv = control_vertical
        from motor import Motor
        self.ml = Motor("left", 8, 9, 6)
        self.mr = Motor("right", 10, 11, 7)

    def set_motor1(self, pd, velocity, slp):
        from time import sleep
        self.vc = velocity          # velocity constant
        self.vc1 = 0
        self.pd = pd
        self.sleep = slp
        if self.cv == 0:  # stop
            self.mr.control(1, 0)
            self.ml.control(1, 0)
        elif self.cv == 1:  # forwards
            if pd < 0:
                self.ml.control(1, self.vc)
                self.mr.control(1, self.vc - self.pd)
                sleep(self.sleep)
                self.ml.control(1, self.vc1)
                self.mr.control(1, self.vc1)
            elif pd > 0:
                self.ml.control(1, self.vc + self.pd)
                self.mr.control(1, self.vc)
                sleep(self.sleep)
                self.ml.control(1, self.vc1)
                self.mr.control(1, self.vc1)
            else:
                self.ml.control(1, self.vc)
                self.mr.control(1, self.vc)
                sleep(self.sleep)
                self.ml.control(1, self.vc1)
                self.mr.control(1, self.vc1)
        elif self.cv == 0:  # reverse
            self.ml.control(0, self.vc)
            self.mr.control(0, self.vc)
            sleep(0.2)

    # def set_motor2(self, left_pd, right_pd):
    #     from time import sleep
    #     vc = 50             # velocity constant
    #     lpd = left_pd
    #     rpd = right_pd
    #
    #     if self.cv == 0:       # stop
    #         self.mr.control(1, 0)
    #         self.ml.control(1, 0)
    #     elif self.cv == 1:         # forwards
    #         self.ml.control(1, vc)
    #         self.mr.control(1, vc)
    #         sleep(0.5)
    #         self.ml.control(1, vc + lpd)
    #         self.mr.control(1, vc + rpd)
    #     elif self.cv == -1:            # reverse
    #         self.ml.control(-1, vc)
    #         self.mr.control(-1, vc)



