from uno_utility import *

deck = generate_deck()

total_players = 0
player_decks = [] #multidimensional array.
starting_hard = 8#how many cards each player gets
stack = [] #this variable stores each card played

def initialize_game():
    start = 0
    end = starting_hard
    for i in range(total_players):
            player_decks.append(deck[start:end])
            del deck[start:end]
    stack.append(deck[-1])
    print(stack)
    #print(player_decks)    


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
    current_card_id = int(input("Select a Card to Play: ")) - 1
    print(current_deck[current_card_id])#making sure it's easier for accessiblity purposes
    if(validate_card(current_deck[current_card_id], stack)):#should give an error for greater than 0 then
        stack.append(current_deck[current_card_id])
        print('Current Stack :', stack[-1])
        return
    else:
        print("Invalid Card, please try again !")
        turn_handler(current_turn)#not sure if it is okay to call the function inside the function ?
    #lay it on stack

    

def game_loop():
    player_turn = 0
    while(check_end_condition()):
        if(player_turn == total_players):
            player_turn == 0
        else:
            turn_handler(player_turn)
            player_turn += 1
            

total_players = int(input("Enter Number of Players : ")) - 1 #easier to do index calculations this way
generate_deck()
initialize_game()
game_loop()
