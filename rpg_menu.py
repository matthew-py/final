import time
from rpg_basement import basement_options
from rpg_basement import basement_menu
from rpg_map import map_of_floors
from starting_game import *
from rpg_upstairs import *


def menu_options_main():
    '''menu for main floor includes list and actions'''
    print("menu:")
# showing where you can go
    print("                     type exit to close")
    print("*area options")
    print("-main floor")
    print("-upstairs master bed room")
    print("-basement")
# telling them what players are on that floor
    print("\n*players nearby")
    print("-josh")
    print("-luke")
# telling them what weapons they currently have
    print("\n*current weapons")
    print("-use gun")
    print("-use poison")


def main_menu():
    '''takes action for menu'''
    player_location = "main floor"
    while player_location == 'main floor':
        # taking use input
        action = input("what action would you like to take: ")
# if else chain baised on their input to decide action
        if action == "main floor":
            print("your already on the main floor")
        elif action == "upstairs master bed room":
            print("you go up the stairs and through the door")
            time.sleep(5)
            print('\n' * 100)
            upstairs_options()
            upstairs_menu()
        elif action == "basement":
            print("you go down the stairs and through the door")
            time.sleep(5)
            basement_options()
            basement_menu()
        elif action == "use gun":
            print("error usage: use gun player_name")
# breaks added for game over to break loop
        elif action == 'use gun josh':
            print("you shot josh but luke noticed and yelled")
            print("game over")
            print("starting new game in 5 seconds")
            time.sleep(5)
            print('\n' * 100)
            game_start()
        elif action == "use gun luke":
            print("you shot luke but josh noticed and yelled")
            print("game over")
            print("starting new game in 5 seconds")
            time.sleep(5)
            print('\n' * 100)
            game_start()
        elif action == "use poison":
            print("error usage use poison player_name")
        elif action == "use poison josh":
            print("you can only use poison on the target")
        elif action == "use poison luke":
            print("print you can only use poison on the target")
        elif action == "exit":
            print("back")
            break
        else:
            print("error try again")
