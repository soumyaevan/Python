import random

class Card:
    Suit_of_Cards = ["Hearts","Diamonds","Clubs","Spades"]
    Value_of_Cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self,suit,value):
        if suit not in Card.Suit_of_Cards or value not in Card.Value_of_Cards:
            raise AttributeError("Invalid Attribute")
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"
class Deck:
    cards = []
    def __init__(self):
        for suit in Card.Suit_of_Cards:
            for value in Card.Value_of_Cards:
                Deck.cards.append(Card(suit,value))
    def count(self):
        return len(Deck.cards)
    def __repr__(self):
        numOfCardsAvailable = self.count()
        return f"Deck of {numOfCardsAvailable} cards"
    def _deal(self,number):
        if self.count() != 0:
            if number >= self.count():
                Deck.cards.clear()
            else:
                del Deck.cards[0:number]
        else:
            raise ValueError("All cards have been dealt")
    def shuffle(self):
        if self.count() == 52:
            random.shuffle(Deck.cards)
            return Deck.cards
        else:
            raise ValueError("Only full decks can be shuffled")
    def deal_card(self):
        card_Dealt = Deck.cards[0]
        self._deal(1)
        return card_Dealt
    def deal_hand(self,number):
        hand_card = []
        for i in range(0,number):
            hand_card.append(Deck.cards[i])
        self._deal(number)
        return hand_card











d = Deck()
#d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
card2 = d.deal_card()
print(card2)
print(d.cards)
print("############")
card2 = d.deal_card()