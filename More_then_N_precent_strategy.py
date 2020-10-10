from base import Envelope, BaseStrategy


class More_then_N_precent_strategy(BaseStrategy):

    def __init__(self):   # constructor
        BaseStrategy.__init__(self)
        self.percent = input("Please enter strategy percentage: ")   # user enters desired percentage

    def play(self):   # More_then_N_precent_strategy.play() uses BaseStrategy.play() and creates the game environment
        BaseStrategy.play(self)

    def perform_strategy(self, counter):   # performs this particular strategy
        percentage = self.percent * 100   # originally given in fraction
        max1 = self.envelopes[0].money   # current maximum value
        if counter < percentage:
            if self.envelopes[counter].money > max1:
                max1 = self.envelopes[counter].money

        else:
            if self.envelopes[counter].money > max1:
                return str(self.envelopes[counter].money)
            else:
                return max1
