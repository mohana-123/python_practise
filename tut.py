# Rock paper scissors game
'''
import random as r

def get_choices():
    com_choices = ['rock', 'paper', 'scissors']
    player_choice = input("Enter a choice (rock, papaer or scissors): ")
    computer_choice = r.choice(com_choices)
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player} and computer chose {computer}")
    if player == computer:
        print("It's a tie!")
    elif player == 'rock':
        if computer == 'scissors':
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers Rock! You lose"
    elif player == 'paper':
        if computer == 'rock':
            return "Paper covers Rock! You win!"
        else:
            return "Scissors cuts paper! You lose"
    elif player == 'scissors':
        if computer == 'paper':
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose"
        

choices = get_choices()
result = check_win(choices['player'],choices['computer'])
print(result)
'''


# Classes
'''
class animal:
    def walk(self):
        print("Walking...")

class dog(animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('woof!')

roger = dog("Roger", 8)
print(roger.name)
print(roger.age)
roger.bark()
roger.walk()
'''


# Modules

# import dog
# from lib import dog

# dog.bark()

# from lib.dog import bark
# bark()


# import sys

# print(sys.builtin_module_names)

# r = lambda n : n*2
# print(r(4))


# map function
'''
num = [1,2,3]

# def double(a):
#     return a*2

r = map(lambda num: num*2, num)
print(list(r))
'''

# filter function
'''
num = [i for i in range(20)]

# def checkeven(a):
#     return a%2 == 0

r = filter(lambda a: a%2 == 0, num)
print(list(r))
'''

# reduce function
'''
expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]
sum = 0
for exp in expenses:
    sum += exp[1]

print(sum)
'''
'''
from functools import reduce

expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]
sum = reduce(lambda a,b: a[1]+b[1], expenses)

print(sum)
'''

# decorators
'''
def logtime(func):
    def wrapper():
        # do something before
        print("before")
        val = func()
        # do something after
        print("after")
        return val
    return wrapper

@logtime
def hello():
    print("Hello!")

hello()
'''

# Docstrings
'''
def increament(n):
    """increment a number"""
    return n+1

print(increament(4))

print(help(increament))
'''

# Annotations
'''
def increament(n: int) -> int:
    return n+1

count: int = 0
'''

# Exceptions
'''
try:
    a = int(input())
    b = int(input())
    result = a/b
    if result == a:
        raise Exception("ah don't divide by one")
    print(result)
except ZeroDivisionError:
    print("Can't divide a number by zero buddy!")
except Exception as error:
    print(error)
finally:
    result = 1
    print("watch out while inputing! Thank you")
'''
'''
class divi_Exception(Exception):
    print("inside the class!")

try:
    raise divi_Exception()
except divi_Exception:
    # print("the class is empty! write any code man!")
    print(divi_Exception)
'''
'''
class DiviException(Exception):
    print("I am inside the class")

try:
    raise DiviException("Something broke")
except DiviException:
    print("exception occured")
'''
'''
class DiviException(Exception):
    pass

try:
    raise DiviException("Something broke")
except DiviException as e:
    print("exception occurred:", e)
'''

# with statement useful in exceptions and file handling
'''
filename = 'ex.txt'

with open(filename, 'r') as finww:
    content = finww.read()
    print(content)
'''





# blackjack card game
import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return (f"{self.rank["rank"]} of {self.suit}")

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
                    {"rank" : "A", "Value" : 11},
                    {"rank" : "2", "Value" : 2},
                    {"rank" : "3", "Value" : 3},
                    {"rank" : "4", "Value" : 4},
                    {"rank" : "5", "Value" : 5},
                    {"rank" : "6", "Value" : 6},
                    {"rank" : "7", "Value" : 7},
                    {"rank" : "8", "Value" : 8},
                    {"rank" : "9", "Value" : 9},
                    {"rank" : "10", "Value" : 10},
                    {"rank" : "J", "Value" : 10},
                    {"rank" : "Q", "Value" : 10},
                    {"rank" : "K", "Value" : 10}
                ]


        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))


    def suffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0: 
                card = self.cards.pop(number)
                cards_dealt.append(card)
        return cards_dealt

class Hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)
    
    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            card_value = int(card.rank["Value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10
        
    def get_value(self):
        self.calculate_value()
        return self.value
    
    def is_blackjack(self):
        return self.get_value() == 21
    
    def display(self):
        print(f"""{"Dealer's" if self.dealer else "Yours"} hand: """)
        for card in self.cards:
            print(card)

        if not self.dealer:
            print("Value: ", self.get_value())
        print()
        

deck = Deck()
deck.suffle()

hand = Hand()
hand.add_card(deck.deal(2))
hand.display()