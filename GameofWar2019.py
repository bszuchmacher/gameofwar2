
# import
import games, cards, bet


class WAR_Card(cards.Card):  # basic class is described in the 'cards' module
    """A virtual card for a card game 'WAR'"""
    ACE_VALUE = 1

    @property  # card value
    def value(self):
        v = WAR_Card.RANKS.index(self.rank) + 2
        return v


class WAR_Deck(cards.Deck):  # basic class is described in the 'cards' module
    """A deck for a card game 'WAR'"""
    MIN_CARDS = 4;  # minimum number of cards in the deck when it is still possible to continue the game

    def populate(self):
        for suit in WAR_Card.SUITS:
            for rank in WAR_Card.RANKS:
                self.add(WAR_Card(rank, suit))  # the 'add' method is described in the 'Deck' class

    @property  # cards left in the deck
    def cards_left(self):
        return len(self.cards)


class WAR_Hand(cards.Hand):  # basic class is described in the 'cards' module
    """A 'WAR' hand - cards in player's hands"""

    def __init__(self, name):
        super().__init__()  # redefining of the basic class construcor
        self.name = name

    @property  # amount of points in a player's hand
    def total(self):
        t = 0
        for card in self.cards:
            t += card.value
        return t

    def __str__(self):
        response = self.name + ":\t" + super().__str__() + "(" + str(self.total) + ")"
        return response


class WAR_Player(WAR_Hand):
    """A player in card game 'WAR'"""

    def __init__(self, name, captured_cards=0):
        super().__init__(name)
        self.captured_cards = captured_cards  # cards which have been collected during the game

    def lose(self):
        print(self.name, "lose.")

    def win(self):
        print(self.name, "win.")

    @property
    def current_cards(self):
        return len(self.cards)

    money = 1000
    score = 0
    bet = 0

    def takeBet(self):
        while True:
            Player.bet = int(input('Enter Your Bet :- '))
            print('\n')
            if Player.bet > Player.money:
                print(f'You have only {Player.money} RS')
                continue
            else:
                break

class WAR_Game(object):
    """Card game 'WAR'"""

    def __init__(self, names):
        self.players = []
        for name in names:
            player = WAR_Player(name)
            self.players.append(player)
        self.deck = WAR_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def reshuffle(self):
        self.deck.clear()
        self.deck.populate()
        self.deck.shuffle()

    def __additional_cards(self, player):
        self.deck.deal([player])
        print(player)

    def play(self):
        self.deck.deal(self.players)
        print("One card for each player:")
        for player in self.players:
            print(player)

        print("\nComparing cards:", end=" ")
        while self.players[0].total == self.players[1].total:
            print("The same value of the cards. One more card for each player:")
            for player in self.players:
                self.__additional_cards(player)
        if self.players[0].total > self.players[1].total:
            self.players[0].win()
            self.players[0].captured_cards += (self.players[0].current_cards + self.players[1].current_cards)
            print(self.players[0].name, ", you have captured",
                  (self.players[0].current_cards + self.players[1].current_cards), "cards.")
        else:
            self.players[1].win()
            self.players[1].captured_cards += (self.players[0].current_cards + self.players[1].current_cards)
            print(self.players[1].name, ", you have captured",
                  (self.players[0].current_cards + self.players[1].current_cards), "cards.")
        # clearing all cards
        for player in self.players:
            player.clear()


def main():
    print("\t\tWelcome to Ben's Game  ----- 'W A R'!\n")
    names = []
    for i in range(2):
        name = input("Enter your name " + str(i + 1) + ": ")
        names.append(name)

    game = WAR_Game(names)

    again = None
    while again != "n":
        if game.deck.cards_left <= WAR_Deck.MIN_CARDS:
            print("\nThere are too little cards left in the deck (", WAR_Deck.MIN_CARDS, "). Reshuffling.")
            game.reshuffle()
        print("\nNow there are:", game.deck.cards_left, "cards in the deck.")
        game.play()
        print("\n\tStatisitcs:")
        print(game.players[0].name, " - ", game.players[0].captured_cards, ".")
        print(game.players[1].name, " - ", game.players[1].captured_cards, ".")
        again = games.ask_yes_no("\nContinue? (y/n): ")
    print("\n\t General statisitcs:")
    print(game.players[0].name, " - ", game.players[0].captured_cards, ".")
    print(game.players[1].name, " - ", game.players[1].captured_cards, ".\n")


main()
input("Press the enter key to exit. ")