from Board import Board
from Dealer import *
from Card import Card
import time
import random


# blackjack game main functions:

def randCard():
    # cards pack:
    cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Queen', 'Jack', 'King', 'Ace']
    return random.choice(cards)  # return a random card


def checkPlayerBet(player, bet):  # check if the player can bet in this amount of money
    if player.getBalance() <= 0:
        print('You broke, time to spend money on other things')
        time.sleep(1)
        exit()
    return bet <= player.getBalance()


def hit():
    ans = str(input("Hit or Stop? H|S:"))
    return ans == 'H'  # keep hit


def bust(Sum):
    return Sum > 21  # bust


def win(pSum, dSum):
    if pSum == dSum:
        return -1  # draw
    return pSum > dSum  # the player won


def endGame(player, board, dealer, winner):
    if winner == -1:
        print('Its a draw!')
    elif winner == 1:
        if bust(dealer.get_sum()):
            print('Dealer bust,', end='')
        print('You win the game!')
        player.addToBalance(board.get_sum())
        player.addToBalance(board.get_sum()/2)  # return the money
    else:
        if bust(player.get_sum()):
            print('You bust,', end='')
        print('You lost the game!')
    if replay():
        board.clear()
        player.clear()
        dealer.clear()
        print('Your remaining money:{}'.format(player.getBalance()))
        return True  # another game
    return False


def replay():
    ans = str(input('Do you want another game? Y|N:'))
    return ans == 'Y'
