# it wont display pin oand balance because they are protected  by using double underscore
class Account:
    def __init__(self, number, pin):
        self.number = number
        self.__pin = pin
        self.__balance = 0

# outputs the balance when correct pin is given
    def show_balance(self,pin):
        if pin == self.__pin:
            return self.__balance

        else:
            return "wrong pin"
