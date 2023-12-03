from display.display import display
from numpad.numpad   import numpad
from motor.motor     import motor

user_input = None
state = 0
volume_input_taken = 0
flowrate_input_taken = 0

# numpad pins
keypad_rows_pins = [9,8,7,6]
keypad_columns_pins = [5,4,3,2]

# motor pins
uart = 13
ai1  = 10
ai2  = 11

# display pins
clk_pin   = 14
mosi_pin  = 15
dc_pin    = 16
reset_pin = 17
cs_pin    = 18

display_inst_1 = display(clk_pin, mosi_pin, dc_pin, reset_pin, cs_pin)
numpad_inst_1 = numpad(keypad_rows_pins, keypad_columns_pins, display_inst_1)
motor_inst_1 = motor(uart, ai1, ai2, display_inst_1, 8)

while True:
    print("state", state)
    # full system sanity check
    if state == 0:
        print("hello moto")

        motor_inst_1.pump_sanity_check(50) # function call pump sanity check
        pump_flag = input("Input 1: ")
        print("            >>>>>>>>>", pump_flag)

        display_inst_1.buzz_check_display() # function call buzzer sanity check
        buzz_flag = input("Input 2: ")
        print("            >>>>>>>>>", buzz_flag)

        state = 1

    #########################################################################
    ### main loop
    # use both of the bottom inputs to calculate the time for bag empty function
    if state == 1:

        print("1")

        if volume_input_taken == 0:
            display_inst_1.data_prompt_volume_display()

            #calling numpad

            while True:
                numpad_volume_result = numpad_inst_1.scankeys('A','B',"mL")

                if numpad_volume_result == None:
                    pass
                elif numpad_volume_result['done'] == 1:
                    print(numpad_volume_result)
                    volume_input_taken = 1
                    volume = int(numpad_volume_result['num'])
                    break


        
        if flowrate_input_taken == 0:
            display_inst_1.data_prompt_flowrate_display()

            #calling numpad
            while True:
                numpad_flowrate_result = numpad_inst_1.scankeys('A','B',"mL/h")
                if numpad_flowrate_result == None:
                    pass
                elif numpad_flowrate_result['done'] == 1:
                    if int(numpad_flowrate_result['num']) <= 1000:
                        print(numpad_flowrate_result)
                        flowrate_input_taken = 1
                        flowrate = int(numpad_flowrate_result['num'])
                        break
                    else:
                        print("not valid")
                        pass
            
            state = 2

    # displaying all inputs 
    if state == 2:

        print("2")

        display_inst_1.display_data(volume,flowrate)


        print("val", volume)
        print("flow", flowrate)

        state = 3


    if state == 3: 

        #we calculat when the bag will finish

        # reset syestem to stage 1 

        user_input = input("reset: ")
        print(user_input)

        if user_input == "d":
            state = 1
            volume_input_taken = 0
            flowrate_input_taken = 0





        print("val", volume)
        print("flow", flowrate)

