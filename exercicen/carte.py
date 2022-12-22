from random import shuffle

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color  
    def __str__(self):
        return f"{self.color}{self.value}"

class DeckCards:
    def __init__(self):
        color = ["S","H","C","D"]
        value = ["A","2","3","4","5","6","7","8","9","X","J","Q","K"] 
        self.cards = []
        for i in color:
            for j in value:
                self.cards.append(Card(j, i))
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            if (i % 13 == 0):
                s += "\n"
            s += str(self.cards[i])
            s += " "
        return s
            
    def shuffle_cards(self):
        shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop(0)


d = DeckCards()

print(d)

d.draw_card()

print(d)