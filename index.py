#TODO : write a database for player using sqllite3
#TODO : add authentication for player turn ig.

import os
import random

deck_color = ["red", "green", "blue", "yellow"]
deck_action = ["draw_two", "skip", "reverse"]
deck_special = ["draw_four", "wild"]
#should add a demiliting string in b/w to seperate out the card name
delimit_char = '|'
deck = []
#need a helper function that resets turn counter

total_players = 0
player_hands = [] #multidimensional array.
hand = 8#how many cards each player gets
stack = [] #this variable stores each card played

def cls():#a util function that allows us to clear the screen on both windows and linux
    os.system('cls' if os.name=='nt' else 'clear')

def generate_deck():
    #generating cards 1-9
    for i in range(4):
        deck.append('0' + delimit_char + deck_color[i])#0 card one of each
        for j in range(9):#TODO: testing, should be 9!!
            for _ in range(2):#adding two number color cards 1-9
                deck.append(str(j + 1) + delimit_char + deck_color[i])
    for i in range(4):
        for j in range(3):#adding two pairs of action cards 
            for _ in range(2):
                deck.append(deck_action[j] + delimit_char + deck_color[i])
    #adding special cards
    for j in range(2):#special cards do not have colors !
        for _ in range(4): #fourth
            deck.append(deck_special[j] + delimit_char)
    print(len(deck))
    random.shuffle(deck)
    return deck

deck = generate_deck()

def initialize_game():
    #add instruction string here.
    stack_card = deck[-1]
    for _ in range(total_players + 1):# + 1 because we subtract 1 from the initial input, i guess i should move this to another variable huh
            player_hands.append(deck[0:hand])
            del deck[0:hand]
    if(deck_action.count(stack_card.split('|')[0]) > 0 or deck_special.count(stack_card.split('|')[0]) > 0):
        #print("Special card on first stack., shuffling back into deck")
        random.shuffle(deck)
        initialize_game()
    else:
        #first card must be a normal card, so 
        stack.append(stack_card)
    
def next_turn(curr_turn, t_plyrs):
    if(rev_flag == False):
        if(curr_turn == t_plyrs):
            return 0
        else:
            return curr_turn + 1
    else:
        if(curr_turn == 0):
            return t_plyrs #this should reverse the order
        else:
            return curr_turn - 1

#check if the card matches the color or number of last card played
#can't use object so have to make do with strings :/
def validate_card(card, stack, hand, player_turn):
    stack = stack[-1].split('|')
    card_valid = card.split('|')#element 1 is card number/type and element 2 is color
    #print(stack , " == ", card_valid, "?")
    if(deck_special.count(card_valid[0]) > 0):
            special_handler(card_valid[0])#add functionality for special cards here
            return True
    if(card_valid[0] == stack[0] or card_valid[1] == stack[1]):#TODO : implement skip, draw_two and reverse
        if(deck_action.count(card_valid[0]) > 0):
            action_handler(card_valid[0], hand, player_turn)
        return True
    else:
        return False
    
def action_handler(action, hand, player_turn):
    #add logic for draw two, rev, skip here
    if(action == "draw_two"):
        for _ in range(2):
            player_hands[next_turn(player_turn, total_players)].append(deck[-1])
    elif(action == "reverse"):
        rev_flag = False if True else True 
    elif(action == "skip"):
        if(player_turn + 1 == total_players):
            player_turn = 0
        else:
            player_turn += 1

def special_handler(action):
    #wild turn will require a prompt to be printed out in next players turn and should be checked for validity
    #add logic for wild and draw four here
    #hint : might be useful to have a buffer variable for the quoted value
    read_in = input("Enter what card color you want on stack : ")
    if(deck_color.count(read_in) > 0):
        stack_card = action + '|' + read_in
        stack.append(stack_card)
    else:
        print("Invalid Card Color, please enter from ", deck_color)
        special_handler(action)
    if(action == "draw_four"):
        for _ in range(4):
            player_hands[next_turn(player_turn, total_players)].append(deck[-1])

def check_end_condition():
    for x in range(total_players):
        if(len(player_hands[x]) < 1):#check if any decks has cards less than 1
            print('Game Ended !, Player {0} wins !'.format(x))
            return False
        else:
            return True

def turn_handler(current_turn):
    #display card
    print("Current Stack :", stack[-1])
    current_hand = player_hands[current_turn] 
    print('Player {0}'.format(current_turn + 1))
    print('Deck : {0}'.format(current_hand))
    print("type d to (d)raw one card from deck.")
    #get input

    #check if hand contains stack, if not, draw until desired card is taken OR
    #player has to manually enter draw <<< went for this approach

    read_in = input("Select a Card to Play: ")

    if(read_in == 'd'):
        current_hand.append(deck[0])
        del deck[0]
        turn_handler(current_turn)
        return
    
    current_card_id = int(read_in) - 1
    print(current_hand[current_card_id])#making sure it's easier for accessiblity purposes
    if(validate_card(current_hand[current_card_id], stack, current_hand, current_turn)):#validating and calling special functions should ideally be two seperate processes
        stack.append(current_hand[current_card_id])
        del current_hand[current_card_id]
        print('Current Stack :', stack[-1])
        cls()
        return
    else:
        print("Invalid Card, please try again !")
        turn_handler(current_turn)
    #lay it on stack


def game_loop():
    global rev_flag 
    rev_flag = False
    global player_turn
    player_turn = 0
    while(check_end_condition()):
        turn_handler(player_turn)
        player_turn = next_turn(player_turn, total_players)

print("Welcome to UNO !, This is a project made for the course Programming Fundamentals, Habib University.")
print("Shuffle Cards from the Deck and try to match the one in the stack !")
print("This game is best played on one computer, with players taking alternating turns entering input.")
print("Group Members : Muhammad Hamza Asad, Dania Salman, Haniya Khan")
print("The game ends when one player runs out of cards to play, note that the player has to physically shout 'UNO!' to declare it")

def set_Players():
    global total_players
    total_players = int(input("Enter Number of Players : ")) - 1 #easier to do index calculations this way
    if(total_players > 5 or total_players < 2):
        print("Total Players cannot be less than 2 and more than 5 !")
        print("Please Try Again.")
        set_Players()

set_Players()
initialize_game()
game_loop()
