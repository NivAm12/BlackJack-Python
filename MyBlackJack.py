from Board import Board
from Dealer import *
from Card import Card
from functions import *
import time
import os

# main:
dealer = Dealer()
player = Player()
board = Board()
balance = int(input('Please enter your balance for the rest of the games: '))
player.setBalance(balance)  # set the money that the player have for the rest of the games
while True:
    time.sleep(1)
    os.system('cls')
    busted = False
    winner = False
    print('Welcome to blackjack game!\n')
    bet = int(input('Please make your bet-->'))
    while not checkPlayerBet(player, bet):
        bet = int(input("You don't have this amount of money, please make a smaller bet-->"))
    player.addToBalance(-bet)  # get the money from the player
    board.set_sum(bet*2)  # the amount to win
    print('The game has stared, look at your hand')
    dealer.add_card(Card(randCard()))  # the first card to the dealer
    board.set_board(player.hand, dealer.hand)
    # 2 cards for the player:
    player.add_card(Card(randCard()))
    player.add_card(Card(randCard()))
    board.set_board(player.hand, dealer.hand)
    board.print_board(player, dealer)
    while hit():  # keep asking for cards
        player.add_card(Card(randCard()))
        board.set_board(player.hand, dealer.hand)
        os.system('cls')
        board.print_board(player, dealer)
        if bust(player.get_sum()):  # over 21
            busted = True
            break

    if not busted:
        os.system('cls')
        board.print_board(player, dealer)
        # add cards to the dealer:
        dealer.add_card(Card(randCard()))
        board.set_board(player.hand, dealer.hand)
        os.system('cls')
        print('Now the dealer will continue: ')
        board.print_board(player, dealer)
        time.sleep(3)  # to show slowly what is happening in the board
        while dealer.get_sum() < 17:  # he has to get another cards
            dealer.add_card(Card(randCard()))
            board.set_board(player.hand, dealer.hand)
            os.system('cls')
            board.print_board(player, dealer)
            if bust(dealer.get_sum()):
                winner = True  # the dealer busted
                break
            time.sleep(3)
        os.system('cls')
        board.print_board(player, dealer)
        if not winner:  # end of the game without the player and the dealer bust:
            winner = win(player.get_sum(), dealer.get_sum())  # check if the player won
    if not endGame(player, board, dealer, winner):  # finish the game and checks if the player want another one
        break



