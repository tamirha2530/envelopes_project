import random


class Envelope:
    def __init__(self):
        """constructor"""
        self.used = False
        self.money = random.randint(1, 100)


class BaseStrategy:
    def __init__(self, envelopes):
        """constructor"""
        self.envelopes = envelopes

    def play(self):    # creates the game environment
        print('You chose "BaseStrategy":')
        for counter in range(100):
            if self.perform_strategy(counter):
                return

    def perform_strategy(self, counter):
        yes_no = input("There are " + str(self.envelopes[counter].money) + " dollars in this envelope. Do you want to take it? answer: y/n")
        self.envelopes[counter].set_used = True
        if counter == 99:
            print("It was the last envelope :( , you need to take it")
            return True
        if yes_no == 'y':
            print("You selected an envelope with "+ str(self.envelopes[counter].money) + " dollars")
            return True
        return False

    @staticmethod
    def display():
        return "- Base Strategy - user select manually envelopes"


class Automatic_BaseStrategy(BaseStrategy):
    def __init__(self, env_arr):
        """constructor"""
        self.env_arr = env_arr

    def play(self):    # creates the game environment
        print('You chose "Automatic Strategy":')
        random_num = random.randrange(0, 100, 1)
        self.preform_strategy(random_num)

    def preform_strategy(self, counter):
        for i in range(100):
            if (i == counter):
                print(f'You got an envelope with {self.env_arr[i].money}$')

    @staticmethod
    def display():
        return "- Automatic Strategy - random selection of an envelope"


class N_max_strategy(BaseStrategy):
    def __init__(self, envelopes):
        """constructor"""
        self.envelopes = envelopes
        self.N = 3

    def get_N(self):
        return self.N

    def play(self):    # creates the game environment
        print('You chose "N Max Strategy":')
        self.perform_strategy(self.N)

    def perform_strategy(self, counter):
        max = 0    # lowest max possible
        for i in range(len(self.envelopes)):
            if (i < counter) and (self.envelopes[i].money > max):
                max = int(self.envelopes[i].money)
        print(f'You got an envelope with {max}$')

    @staticmethod
    def display():
        return "- N Max Strategy - returns envelope after N max values"

class More_then_N_percent_group_strategy(BaseStrategy):
    def __init__(self, envelopes, percent):
        """constructor"""
        self.envelopes = envelopes
        self.percent = percent

    def play(self):    # creates the game environment
        print('You chose "More Than N Precent Group Strategy":')
        self.perform_strategy(self.percent)

    def perform_strategy(self, counter):   # performs this particular strategy
        percentage = float(counter) * 100   # turns percent into number
        max1 = self.envelopes[0].money   # current maximum value
        for i in range(len(self.envelopes)):
            if (i < percentage):
                if self.envelopes[i].money > max1:
                    max1 = self.envelopes[i].money
        print(f'You got an envelope with {max1}$')

    @staticmethod
    def display():
        return "- More Than N Precent Group Strategy - returns an envelope with more money than that in the highest of N% group"
