import random


class Envelope:
    def __init__(self):
        """constructor"""
        self.used = False
        self.money = random.randint(1, 100)

    def get_used(self):
        return self.used

    def get_money(self):
        return self.money

    def set_used(self,use):
        self.used = use

    def set_money(self,money):
        self.money = money


class BaseStrategy:

    def __init__(self, envelopes):
        """constructor"""
        self.envelopes = envelopes

    def play(self):
        for counter in range(100):
            if self.perform_strategy(counter):
                return



    def perform_strategy(self, counter):
        yes_no = input("there are " + str(self.envelopes[counter].get_money()) + " dollars in this envelope. Do you want to take it? answer: y/n")
        self.envelopes[counter].set_used = True
        if counter == 99:
            print("it was the last envelope :( , you need to take it")
            return True

        if yes_no == 'y':
            print("You selected this envelope with "+ str(self.envelopes[counter].get_money()) + " dollars")
            return True

        return False






    @staticmethod
    def display():
        return "Base Strategy - user select manually envelopes"
