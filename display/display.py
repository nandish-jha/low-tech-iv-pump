from display.ST7735 import *
from display.sysfont import sysfont
from machine import SPI,Pin

import time
import math

class display:
    def __init__(self, clk_pin, mosi_pin, dc_pin, reset_pin, cs_pin):
        spi = SPI(1, baudrate=15625000, polarity=0, phase=0, bits=8, sck=clk_pin, mosi=mosi_pin, miso=None)
        self.tft = TFT(spi, dc_pin, reset_pin, cs_pin)
        self.tft.initr()
        self.tft.rgb(False)
        self.tft.rotation(1)
        # system startup screen
        self.tft.fill(TFT.BLACK)
        self.tft.text((5, 5), "System     starting...", TFT.WHITE, sysfont, 2)
        time.sleep(3)




    def sanity_check(self):
        print("start (display.py))")
        self.tft.fill(TFT.PURPLE)
        self.tft.text((5, 5), "Hello World", TFT.WHITE, sysfont, 2)
        self.tft.text((5, 25), "Hello World", TFT.WHITE, sysfont, 2)
        time.sleep_ms(1000)
        print("end")




    def input_check(self, num):
        print("start (input_test)")
        self.tft.fill(TFT.CYAN)
        self.tft.text((5, 5), str(num), TFT.BLACK, sysfont, 2)
        print("end (input_test)")




    def pump_check_display(self):
        # checking/running sanity for pump screen
        self.tft.fill(TFT.CYAN)
        self.tft.text((5, 5), "Checking   pump...", TFT.BLACK, sysfont, 2)
        time.sleep_ms(500)

    def pump_check(self):
        self.tft.fill(TFT.CYAN)
        self.tft.text((5, 5), "Is pump    running?", TFT.BLACK, sysfont, 2)
        self.tft.text((5, 70), "A for yes", TFT.BLACK, sysfont, 2)
        self.tft.text((5, 90), "B for no", TFT.BLACK, sysfont, 2)

        # # when pump has stopped, wait for ack
        # if ack == "a":
        #     self.tft.fill(TFT.CYAN)
        #     self.tft.text((5, 5), "Pump good", TFT.BLACK, sysfont, 2)
        #     flag = 1
        #     time.sleep_ms(3000)

        # elif ack == "b":
        #     self.tft.fill(TFT.CYAN)
        #     self.tft.text((5, 5), "Pump bad", TFT.RED, sysfont, 2)
        #     flag = 0
        #     time.sleep_ms(3000)
        #     # put function to stop the whole system (coz pump is bad)
        # print("end (pump_check)")
        # return flag




    def buzz_check_display(self):
        # checking/running sanity for buzzer screen
        self.tft.fill(TFT.CYAN)
        self.tft.text((5, 5), "Checking   buzzer...", TFT.BLACK, sysfont, 2)
        time.sleep_ms(3000)
        # taking user ack for pump running
        self.tft.fill(TFT.CYAN)
        self.tft.text((5, 5), "Is buzzer  running?", TFT.BLACK, sysfont, 2)
        self.tft.text((5, 70), "A for yes", TFT.BLACK, sysfont, 2)
        self.tft.text((5, 90), "B for no", TFT.BLACK, sysfont, 2)

    def buzz_check(self, flag, ack):
        if (flag == 1):
            print("start (buzz_check)")
            # when buzzer has stopped, wait for ack
            if ack == "a":
                self.tft.fill(TFT.CYAN)
                self.tft.text((5, 5), "Buzzer good", TFT.BLACK, sysfont, 2)
                flag = 1
                time.sleep_ms(3000)

            elif ack == "b":
                self.tft.fill(TFT.CYAN)
                self.tft.text((5, 5), "Buzzer bad", TFT.RED, sysfont, 2)
                flag = 0
                time.sleep_ms(3000)
                # put function to stop the whole system (coz buzzer is bad)
            print("end (pump_check)")
        elif (flag == 0):
            print("pump is not running")

        return flag




    def shutdown(self):
        # system shut down if bad buzzer
        self.tft.fill(TFT.BLACK)
        self.tft.text((5, 5), "System     shut       down", TFT.RED, sysfont, 4)
        time.sleep_ms(3000)




    def data_prompt_volume_display(self):
        self.tft.fill(TFT.CYAN)
        self.tft.text((5, 5), "Enter      volume     in mL", TFT.BLACK, sysfont, 2)

    def data_prompt_volume(self, num_vol, units):
        self.tft.fill(TFT.CYAN)
        self.tft.text((5, 5), str(num_vol) + " " + units, TFT.BLACK, sysfont, 2)

        self.tft.text((5, 45), "A for yes", TFT.BLACK, sysfont, 2)
        self.tft.text((5, 75), "B for clear", TFT.BLACK, sysfont, 2)




    def data_prompt_flowrate_display(self):
        self.tft.fill(TFT.CYAN)
        self.tft.text((5, 5), "Enter      flow rate  in mL/h", TFT.BLACK, sysfont, 2)

    # def data_prompt_flowrate(self,num_fr):
    #     self.tft.fill(TFT.CYAN)
    #     self.tft.text((5, 5), "You entered" + str(num_fr) + " mL/h", TFT.BLACK, sysfont, 2)

    #     self.tft.text((5, 45), "A for yes", TFT.BLACK, sysfont, 2)




    def display_data(self, volume, flow_rate):
        self.tft.fill(TFT.CYAN)
        self.tft.text((5, 5), "Volume:    " + str(volume) + " mL", TFT.BLACK, sysfont, 2)
        self.tft.text((5, 45), "Flow rate: " + str(flow_rate) + " mL/h", TFT.BLACK, sysfont, 2)

