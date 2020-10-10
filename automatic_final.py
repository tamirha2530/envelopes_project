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

class Automatic_BaseStrategy(BaseStrategy):
    def __init__(self, env_arr):
        """constructor"""
        self.env_arr = env_arr

    def play(self):
        random_num = random.randrange(0, 100, 1)
        self.preform_strategy(random_num)

    def preform_strategy(self, counter):
        for i in range(100):
            if (i == counter):
                print(f'you got an envelope with {self.env_arr[i].get_money()}$')

    @staticmethod
    def display():
        return "Automatic Strategy - random selection of an envelope"

