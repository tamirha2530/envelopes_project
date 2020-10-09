import random


class Envelope:
    def __init__(self):
        """constructor"""
        self.used = False
        self.money = random.randint(1, 100)

    def get_money(self):
        return self.money

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


class N_max_strategy(BaseStrategy):
    def __init__(self, envelopes):
        """constructor"""
        self.envelopes = envelopes
        self.N = 3

    def get_N(self):
        return self.N

    def play(self):
        print('100 envelopes on the line. Which one will you choose? How much money will you get? N number strategy is unfolding:')
        counter = self.N
        self.perform_strategy(counter)

    def perform_strategy(self, counter):
        max = 0
        num = 0
        for i in range(len(self.envelopes)):
            if (num < counter) and (self.envelopes[i].get_money() > max):
                max = int(self.envelopes[i].get_money())
                num = num + 1
        print(f'you got an envelope with {max}$')

    @staticmethod
    def display():
        return "N Max Strategy - returns envelope after N max values"



