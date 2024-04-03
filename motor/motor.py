import machine
import utime

class motor:

    def __init__(self, uart, ai1, ai2, display_class, frequ):
        
        print('Pump on with frequency: ', frequ)
        self.display_inst_1 = display_class

        self.mtr_PWMa = machine.PWM(machine.Pin(uart))
        self.mtr_AI2 = machine.Pin(ai1, machine.Pin.OUT)
        self.mtr_AI1 = machine.Pin(ai2, machine.Pin.OUT)
        
        self.mtr_PWMa.freq(frequ)
        self.mtr_AI1.value(1)
        self.mtr_AI2.value(0)
        self.mtr_PWMa.duty_u16(0)



    def pump_sanity_check(self, duty_cycles_p = 100):
        self.display_inst_1.pump_check_display()

        duty_cycles = 65535 * (duty_cycles_p/100)
        self.mtr_PWMa.duty_u16(int(duty_cycles))
        utime.sleep(3)
        self.mtr_PWMa.duty_u16(0)

        self.display_inst_1.pump_check()


    
    def pump_on(self, duty_cycles_p):
        print('Pump on with duty cycle: ', duty_cycles_p)
        duty_cycles = 65535 * (duty_cycles_p/100)
        self.mtr_PWMa.duty_u16(int(duty_cycles))
