class PDControl:
    """calculate PD control value for motor based off the error value from sensors"""
    def __init__(self):
        print('PD')

    def us_pdcontrol(self, l_error1, l_error2, r_error1, r_error2, time1, time2):
        us_p = 0.26
        us_d = 0.05
        self.error1 = l_error1 - r_error1
        self.error2 = l_error2 - r_error2
        self.de = self.error1 - self.error2
        self.dt = time1 - time2
        self.de_dt = self.de/self.dt
        us_pd = us_p*self.error1 - us_d*self.de_dt
        return us_pd

    # def ir_pdcontrol(self, ir_error1, ir_error2, time1, irp): #todo
    #     self.irp = irp
    #     ir_d = 0.01
    #     ir_de = ir_error1 - ir_error2
    #     ir_dt = time1
    #     ir_pd = self.irp*ir_error1 - ir_de
    #     ir_p = self.irp*ir_error1
    #     return ir_pd















