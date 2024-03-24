class Controller:
    def __init__(self):
        self.current_error = 0
        self.previous_error = 0
        self.acumulated_error = 0

    def calc_current_error(self, setpoint, VP):
        self.current_error = setpoint - VP
        return self.current_error

    def calc_acumulated_error(self):
        self.acumulated_error += self.current_error
        return self.acumulated_error

    def calc_previous_error(self):
        self.previous_error = self.current_error-self.previous_error
        return self.previous_error

    def PID(self, setpoint, Kp, Ki, Kd, VP):
        u_k = Kp*self.calc_current_error(setpoint, VP) + Ki * \
            self.calc_acumulated_error() + Kd*self.calc_previous_error()
        return u_k
