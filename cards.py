# Сards module
# A set of basic classes for various cards games.

class Card(object):
    """A virtual card"""
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
    SUITS = ["♤", "♡", "♢", "♧"]

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            response = "'" + self.rank + " " + self.suit + "'"
        else:
            response = "XX"
        return response

    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand(object):
    """'A hand' - set of players cards"""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            response = ""
            for card in self.cards:
                response += str(card) + " "
        else:
            response = "<empty>"
        return response

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """A deck of cards"""

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't deal anymore: no more cards!")
class Shekels():

    def __init__(self, total=50):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def take_bet(Shekels):

        while True:

            try:
                shekels.bet = int(input("How many chips would you like to bet?: "))
            except:
                print("Sorry please provide an intenger")
            else:
                if shekels.bet > shekels.total:
                    print(f"Sorry, you do not have enough chips! You have: {chips.total}")
                else:
                    break

if __name__ == "__main__":
    print("This is a playing cards module.")
    input("Press the enter key to exit. ")