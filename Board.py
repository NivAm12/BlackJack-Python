from Card import Card
from Dealer import *


class Board:
    def __init__(self):
        # empty board
        self.dealerHand = []
        self.playerHand = []
        self.betSum = 0

    def set_sum(self, num):
        self.betSum = num

    def set_board(self, playerCards, dealerCards):  # set the board state
        self.dealerHand = dealerCards
        self.playerHand = playerCards

    def get_sum(self):
        return self.betSum

    def print_board(self, player, dealer):
        print("Dealer:   dealer hand sum:{}\n".format(dealer.get_sum()))
        # dealer cards
        for ca in self.dealerHand:
            print('[ '+str(ca)+' ]', end=' ')
        print('\n')
        #  player cards
        print("Player :  player hand sum:{}                 bet sum:{}\n".format(player.get_sum(), self.betSum))
        for ca in self.playerHand:
            print('[ '+str(ca)+' ]', end=' ')
        print('\n')

    def clear(self):
        self.playerHand = []
        self.dealerHand = []
        self.betSum = 0

