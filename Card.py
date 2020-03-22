class Card:
    def __init__(self):
        self.value = ' '

    def __init__(self, value):
        self.value = value

    def setCard(self, value):  # the name of the card type
        self.value = value

    def getCard(self):
        return self.value

    def __str__(self):  # print the card
        return '%s' % self.value

