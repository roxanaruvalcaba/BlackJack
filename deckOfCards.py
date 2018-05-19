
# Blackjack: I created the object "card", the object "deck" that used "card",
# the object "player" that used "deck", and the object blackjack that used
# "deck" and "player" 

import random # used for sorting the deck

class card(object):
# cards have a suit and numerical value
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def get_suit(self):
        return self.suit
    
    def get_value(self):
        return self.value

class deck(card): 
# deck is made up of 52 cards. There are four suits and the J,K,Q are all 
# represented as "10" in the "values". The deck can be shuffled and I wrote
# the getters of the members for the deck objects.

    def __init__(self):
        self.deckSuits = ["heart", "spade", "club", "diamond"]
        self.deckValue = [2,3,4,5,6,7,8,9,10,10,10,10,"A"]
        self.cards=[]
        
        for i in range (0,len(self.deckSuits)):
            for j in range (0,len(self.deckValue)):
                self.cards.append(card(self.deckSuits[i],self.deckValue[j]))
  
    def get_card_list(self):
        return self.cards  
    
    def get_card(self,k):
        return self.cards[k]
    
    def print_cards(self):
        for i in range (0,len(self.cards)):
            print(self.cards[i].get_suit(), self.cards[i].get_value(),i)
                        
    def shuffle(self,swaps):
        for i in range (0,swaps):
            k1 = random.randint(0,len(self.cards)-1)
            k2 = random.randint(0,len(self.cards)-1)
            tempCard = self.cards[k1]
            self.cards[k1] = self.cards[k2]
            self.cards[k2] = tempCard
         
class player(object):
# player can be either the player or the dealer. The player starts with 20 
# coins and a score of 0. They get cards in their hand by having them dealt to
# them by the "deal" function. The player will want to be able to see their 
# hand and compare their sum to that of the player they are playing against.
    def __init__(self, deck):
        self.hand = []
        self.coins = 20
        self.score = 0
        self.dealtCards=[]
        self.deck = deck
        self.sumOfHand = 0
        self.showHand = []
        
    def deal(self,numberOfCards):
        for i in range (0, numberOfCards):
            self.hand.append(self.deck.cards.pop(0))
        return self.hand

    def sum_Hand(self):
        self.sumOfHand = 0        
        for i in self.hand:
            if i.value == "A":
                print(self.show_Hand())
                i.value = int(input ("Treat Ace as 1 or 11? "))
            self.sumOfHand += i.value
        return self.sumOfHand 
    
    def show_Hand (self):
        self.showHand = []
        
        for i in self.hand:
            self.showHand.append(i.value)
        return (self.showHand)

class blackjack(player):
# If the player is closer to the sum of 21 than the dealer without going over 
# they win 5 coins! If they are not closer or go over they lose 5 coins :(
# If the sum is the same as that of the dealer, no coins are given or taken
    
# In this instance of blackjack, each game costs the player 5 coins. There is 
# only one player playing against the dealer. They can't do fancy stuff like
# split or ask for insurance. In the reset function the player starts another
# blackjack game against the dealer. A new deck is started when there are not 
# enough cards to be played with. The value of an Ace has to be decided when
# it first comes up. The player also decides what the value of the Ace is if 
# the dealer gets an Ace
    
    def __init__(self):
        self.deckOfCards = deck()
        self.deckOfCards.shuffle(100)
        self.playerOne = player(self.deckOfCards)
        self.dealer = player(self.deckOfCards)
        self.playerOne.hand = self.playerOne.deal(2)
        self.dealer.hand = self.dealer.deal(2)
        self.bust = False
        self.proceed = "yes"     
        
    def check_Hands(self):
        message = ""
        while self.dealer.sum_Hand() < self.playerOne.sum_Hand() or self.playerOne.sum_Hand() == self.dealer.sum_Hand() and self.dealer.sum_Hand() < 21: 
            self.new_Deck_Check(1)
            self.dealer.deal(1)
            print("Dealer cards are",self.dealer.show_Hand(),".")
        if self.dealer.sum_Hand() > 21:
            self.playerOne.coins += 5            
            print("You won! Dealer busted. Your total coins are " + str(self.playerOne.coins))
        elif self.playerOne.sum_Hand() < self.dealer.sum_Hand():
            self.playerOne.coins -= 5
            message = "You lost five coins. Your total coins are " + str(self.playerOne.coins)
        if self.playerOne.sum_Hand() == self.dealer.sum_Hand() and self.playerOne.sum_Hand() == 21:
            print("It's a tie! We both have 21")
            message = "Your total coins are " + str(self.playerOne.coins)
        print("Your sum is " + str(self.playerOne.sum_Hand()) + ". Dealer sum is " + str(self.dealer.sum_Hand()) + ".")
        print(message)
        
    def reset(self):
        if self.playerOne.coins<5:
            print("Sorry, you do not have enough coins")
            return
        elif self.proceed == "yes":
            self.bust = False
            self.deckOfCards.shuffle(100)
            self.playerOne.hand = []
            self.dealer.hand = []
            self.new_Deck_Check(4)
            self.playerOne.hand = self.playerOne.deal(2)
            self.dealer.hand = self.dealer.deal(2)
            print("Your total coins are " + str(self.playerOne.coins))
            
    def new_Deck_Check(self,n):
            if len(self.deckOfCards.cards) < n:
                print("Sorry ran out of cards. Need to get a new deck")
                self.deckOfCards = deck()
                self.deckOfCards.shuffle(100)
                self.playerOne.deck = self.deckOfCards 
                self.dealer.deck = self.deckOfCards 
            return
                 
    def play(self):

 
        while self.proceed == "yes" and self.bust == False and self.playerOne.coins >= 5:
            print("\nYour sum is "+str(self.playerOne.sum_Hand())+". Your cards are " + str(self.playerOne.show_Hand()) + ". My top card is " + str(self.dealer.hand[1].value) + ".", end = "")
            self.proceed = input("Would you like a card? Enter yes or no: ")
            if self.proceed == "yes":
                self.new_Deck_Check(1)
                self.playerOne.deal(1)
                print("Your cards are",self.playerOne.show_Hand())
            if self.playerOne.sum_Hand() > 21:
                self.bust = True
                self.playerOne.coins -= 5
                print("You went over! Your sum is " + str(self.playerOne.sum_Hand())+ ". Give me yo coins!!!")
                print("Your total coins are " + str(self.playerOne.coins)+".")
                self.proceed = input("Would you like to play again? Enter yes or no: ")
                if self.proceed == "yes":
                    self.reset()
            if self.proceed == "no":
                self.check_Hands()
                self.proceed = input("Would you like to play again? Enter yes or no: ")
                if self.proceed == "yes":
                    self.reset()
        print ("Thank you for Playing! Your total coins are: ", self.playerOne.coins)
                                   
if __name__=='__main__':
    game = blackjack()
    game.play()
    
    
    
    
