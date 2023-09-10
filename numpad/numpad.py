from machine import Pin
import utime
import sys

class numpad:

    matrix_keys = [['1', '2', '3', 'A'],
                   ['4', '5', '6', 'B'],
                   ['7', '8', '9', 'C'],
                   ['*', '0', '#', 'D']]

    col_pins = []
    row_pins = []

    ## number entered by user
    user_input = []

    def __init__(self, keypad_rows, keypad_columns, display_class):
        self.display_inst_1 = display_class
        for x in range(0, 4):
            self.row_pins.append(Pin(keypad_rows[x], Pin.OUT))
            self.row_pins[x].value(1)
            self.col_pins.append(Pin(keypad_columns[x], Pin.IN, Pin.PULL_DOWN))
            self.col_pins[x].value(0)

    def scankeys(self, confirmation_key, clear, unit):

        for row in range(4):
            for col in range(4):
                self.row_pins[row].high()
                done = 0

                if self.col_pins[col].value() == 1:
                    print("You have pressed:", self.matrix_keys[row][col])
                    if(col == 3 or (row == 3 and col != 1)):
                        if (self.matrix_keys[row][col] == confirmation_key):
                            done = 1
                            # return done
                        if (self.matrix_keys[row][col] == clear):
                            for x in range(0, len(self.user_input)):
                                self.user_input.pop()

                    else:
                        key_press = int(self.matrix_keys[row][col])
                        self.user_input.append(key_press)

                    utime.sleep(0.3)

                    a = ""
                    for i in range(0, len(self.user_input)):
                        a = a + str(self.user_input[i])

                    print(a)
                    self.display_inst_1.data_prompt_volume(a, unit)

                    if done == 1:
                        for x in range(0, len(self.user_input)):
                            self.user_input.pop()


                    obj1 = dict()
                    obj1['done'] = done
                    obj1['num'] = a
                    return obj1

            self.row_pins[row].low()

        def scankeys_general(self):
            #this only accepts inputs A an B in stage 0
            print("hshdh")
 
    
   
            