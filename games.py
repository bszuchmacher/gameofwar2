
# Games module

class Player(object):
    """A virtual player"""
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        response = self.name + ":\t" + str(self.score)
        return response

def ask_yes_no(question):
    """Asks question yes/no"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Asks a number in the range low:high"""
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
        except ValueError:
            print("You have to enter a number in the range ", low, ":", high, "!")
            continue
    return response

if __name__ == "__main__":
    print("This is the game module.")
    input("Press the enter key to exit. ")