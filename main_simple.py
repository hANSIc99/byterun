# https://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html



from imghdr import what


class Interpreter:
    def __init__(self):
        self.stack = []
        self.environment = {}

    def STORE_NAME(self, name): # value to store most be first pushed on the stack
        val = self.stack.pop()
        self.environment[name] = val


    def LOAD_NAME(self, name): # load value of associate variable to the stack
        # >>>> LOAD_FAST
        val = self.environment[name] 
        self.stack.append(val)

    def parse_argument(self, instruction, argument, what_to_execute): 
        # diese methode ordnet die argumente (numbers, names) zu den instruktionen zu
        # das argument an der instruction selbst ist nur ein index zu dem argumentenliste in what_to_execute
        
        """ Understand what the argument to each instruction means"""
        numbers = ['LOAD_VALUE']
        names = ['LOAD_NAME', 'STORE_NAME']

        if instruction in numbers:
            argument = what_to_execute['numbers'][argument]
        elif instruction in names:
            argument = what_to_execute['names'][argument]

        return argument

    def LOAD_VALUE(self, number): # >>>> LOAD_CONST
        self.stack.append(number)

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def ADD_TWO_VALUES(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num + second_num
        self.stack.append(total)

    def run_code(self, what_to_execute):

        instructios = what_to_execute['instructions'] # list

        
        for each_step in instructios:
            instruction, argument = each_step # tuple
            argument = self.parse_argument(instruction, argument, what_to_execute)
            bytecode_method = getattr(self, instruction)

            if argument is None:
                bytecode_method()
            else:
                bytecode_method(argument)

            # if instruction == 'LOAD_VALUE':
            #     self.LOAD_VALUE(argument)
            # elif instruction == 'ADD_TWO_VALUES':
            #     self.ADD_TWO_VALUES()
            # elif instruction == 'PRINT_ANSWER':
            #     self.PRINT_ANSWER()
            # elif instruction == 'STORE_NAME':
            #     self.STORE_NAME(argument)
            # elif instruction == 'LOAD_NAME':
            #     self.LOAD_NAME(argument)


if __name__ == '__main__':


    interpreter = Interpreter()

    # what_to_execute = {
    #     "instructions": [("LOAD_VALUE", 0),  # the first number
    #                     ("LOAD_VALUE", 1),  # the second number
    #                     ("ADD_TWO_VALUES", None),
    #                     ("LOAD_VALUE", 2),
    #                     ("ADD_TWO_VALUES", None),
    #                     ("PRINT_ANSWER", None)],
    #     "numbers": [7, 5, 8] }


    what_to_execute = {
        "instructions": [("LOAD_VALUE", 0),
                         ("STORE_NAME", 0),
                         ("LOAD_VALUE", 1),
                         ("STORE_NAME", 1),
                         ("LOAD_NAME", 0),
                         ("LOAD_NAME", 1),
                         ("ADD_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "numbers": [1, 2],
        "names":   ["a", "b"] }

    interpreter.run_code(what_to_execute)