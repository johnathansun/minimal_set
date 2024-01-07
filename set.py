import random
from itertools import product
import re

class Set():

    def __init__(self):
        self.types = ['1', '2', '3']
        self.colors = ['R', 'G', 'B']
        self.shapes = ['D', 'O', 'S']
        self.patterns = ['S', 'F', 'E']

        combos = list(product(self.types, self.colors, self.shapes, self.patterns))
        random.shuffle(combos)
        combos = [''.join(map(str, c)) for c in combos]
        self.play_area, self.deck = combos[:16], combos[16:]
        self.playing = True

    def print_play_area(self, cards):
        for i in range(0, len(cards), 4):
            print("  ".join(cards[i:i+4]))

    def check(self, card1, card2, card3):
        for i in range(4):
            if card1[i] == card2[i] == card3[i]:
                continue
            elif card1[i] != card2[i] and card1[i] != card3[i] and card2[i] != card3[i]:
                continue
            else:
                return False
        return True
    
    def get_cards(self, indexes):
        return [self.play_area[i] for i in indexes]

    def play(self):
        while self.playing:
            print("Current play area")
            self.print_play_area(self.play_area)
            guess = input("Enter indexes 1-16 separated by spaces: ").split()
            if not all(re.match(r"^[0-9 ]+$", s) for s in guess):
                print("Invalid input")
                continue
            index = [int(i) - 1 for i in guess]
            if not all(i in range(16) for i in index):
                print("Out of bounds")
                continue
            cards = self.get_cards(index)
            if self.check(cards[0], cards[1], cards[2]):
                print("Set!")
                checkmark = self.play_area
                for i in input:
                    checkmark[i] = u'\u2713' * 4
                    self.play_area[i] = self.deck.pop()
                self.print_play_area(checkmark)
            else:
                print("Not a set")

            if len(self.deck) == 0:
                    self.playing = False
                    print("You win!")
        
set = Set()
set.play()