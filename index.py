from uno_utility import *

#TODO : write a database for player using sqllite3

deck = generate_deck()

total_players = 0
player_decks = [] #multidimensional array.
hand = 8#how many cards each player gets
stack = [] #this variable stores each card played

def initialize_game():
    for i in range(total_players + 1):# + 1 because we subtract 1 from the initial input, i guess i should move this to another variable huh
            player_decks.append(deck[0:hand])
            del deck[0:hand]
    stack.append(deck[-1])
    print("Current Stack :", stack[-1])
 
def action_handler():
    #add logic for draw two, rev, skip here
    pass

def special_handler():
    #add logic for wild and draw four here
    #hint : might be useful to have a buffer variable for the quoted value
    pass

def check_end_condition():
    for x in range(total_players):
        if(len(player_decks[x]) < 1):#check if any decks has cards less than 1
            print('game has ended')
            return False
        else:
            return True

def turn_handler(current_turn):
    #display card
    current_deck = player_decks[current_turn] 
    print('Player {0}'.format(current_turn + 1))
    print('Deck : {0}'.format(current_deck))
    #get input
    current_card_id = int(input("Select a Card to Play: ")) - 1
    print(current_deck[current_card_id])#making sure it's easier for accessiblity purposes
    if(validate_card(current_deck[current_card_id], stack)):#should give an error for greater than 0 then
        stack.append(current_deck[current_card_id])
        del current_deck[current_card_id]
        print('Current Stack :', stack[-1])
        return
    else:
        print("Invalid Card, please try again !")
        turn_handler(current_turn)#not sure if it is okay to call the function inside the function ?
    #lay it on stack

    

def game_loop():
    player_turn = 0
    while(check_end_condition()):
        turn_handler(player_turn)
        if(player_turn == total_players):
            player_turn = 0
        else:
            player_turn += 1
        
total_players = int(input("Enter Number of Players : ")) - 1 #easier to do index calculations this way
initialize_game()
game_loop()
