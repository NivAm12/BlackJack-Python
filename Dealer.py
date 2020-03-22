from Card import Card


class Dealer:
    def __init__(self):
        self.hand = []  # player hand
        self.sum = 0

    def add_card(self, card):
        self.hand.append(card)  # add the card to the player hand
        self.handSum()  # add the value of the card

    def get_sum(self):
        return self.sum

    def handSum(self):
        temp = 0
        for item in self.hand:
            if item.getCard() in ['Queen', 'King', 'Jack']:  # special cards
                temp += 10
            elif item.getCard() == 'Ace':  # ace card treatment
                if temp + 11 > 21:
                    temp += 1
                else:
                    temp += 11
            elif 1 <= int(item.getCard()) <= 10:  # regular cards
                temp += int(item.getCard())
        self.sum = temp

    def clear(self):
        self.hand.clear()
        self.sum = 0


class Player(Dealer):
    def __init(self):
        super.__init__()
        self.balance = 0  # amount of money that the player have

    def setBalance(self, bal):
        self.balance = bal

    def getBalance(self):
        return self.balance

    def addToBalance(self, val):
        self.balance += val

