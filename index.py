import random

deck_color = ["red", "green", "blue", "yellow"]
deck_action = ["draw_two", "skip", "reverse"]
deck_special = ["draw_four", "wild"]
#should add a demiliting string in b/w to seperate out the card name
delimit_char = '|'
final_deck = []

def generate_deck():
    #generating cards 1-9
    for i in range(4):
        for j in range(9):
            final_deck.append( str(j + 1) + delimit_char + deck_color[i])
    for i in range(4):
        for j in range(3):
            for k in range(2):
                final_deck.append(deck_action[j] + delimit_char + deck_color[i])
    random.shuffle(final_deck)
    #print(final_deck)
        
total_players = 0
player_decks = [] #multidimensional arrays.
starting_hard = 8
stack = [] #this variable stores each card played

def initialize_game():
    start = 0
    end = starting_hard
    for i in range(total_players):
            player_decks.append(final_deck[start:end])
            start += starting_hard
            end += starting_hard 
    #print(player_decks)

def validate_card(card):
    if(card == stack[-1]):
    #check if the card matches the color or number of last card played
    #can't use object so have to make do with strings :/


def check_end_condition():
    for x in range(total_players):
        if(len(player_decks[x]) < 1):#check if any decks has cards less than 1
            return True
        else:
            return False

def turn_handler(current_turn):
    #display card
    current_deck = player_decks[current_turn] 
    print('Player {0}'.format(current_turn + 1))
    print('Deck : {0}'.format(current_deck))
    #get input
    current_card_id = int(input("Select a Card to Play: "))
    print(current_deck[current_card_id - 1])#making sure it's easier for accessiblity purposes
    validate_card(current_deck[current_card_id])
    #lay it on stack

    

def game_loop():
    player_turn = 0
    turn_handler(player_turn)
    while(check_end_condition()):
        
        if(player_turn == 2):
            player_turn == 0
        else:
            player_turn += 1
            

    


total_players = int(input("Enter Number of Players : ")) - 1 #easier to do index calculations this way
generate_deck()
initialize_game()
game_loop()
