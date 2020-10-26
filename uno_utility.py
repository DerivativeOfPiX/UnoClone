import os
import random

deck_color = ["red", "green", "blue", "yellow"]
deck_action = ["draw_two", "skip", "reverse"]
deck_special = ["draw_four", "wild"]
#should add a demiliting string in b/w to seperate out the card name
delimit_char = '|'
deck = []

def cls():#a util function that allows us to clear the screen on both windows and linux
    os.system('cls' if os.name=='nt' else 'clear')

def generate_deck():
    #generating cards 1-9
    for i in range(4):
        deck.append('0' + delimit_char + deck_color[i])#0 card one of each
        for j in range(9):
            for k in range(2):#adding two number color cards 1-9
                deck.append( str(j + 1) + delimit_char + deck_color[i])
    for i in range(4):
        for j in range(3):#adding two pairs of action cards 
            for k in range(2):
                deck.append(deck_action[j] + delimit_char + deck_color[i])
    #adding special cards
    for j in range(2):#special cards do not have colors !
        for k in range(4): #fourth
            deck.append(deck_special[j] + delimit_char)
    random.shuffle(deck)
    return deck

#check if the card matches the color or number of last card played
#can't use object so have to make do with strings :/
def validate_card(card, stack):
    stack = stack[-1].split('|')
    card_valid = card.split('|')#element 1 is card number/type and element 2 is color
    if(len(card_valid) > 1): #checking if the card is special or not
        if(card_valid[0] == stack[0] or card_valid[1] == stack[1]):
            return True
    elif(len(card_valid) == 1):
        return True
    else:
        return False









    