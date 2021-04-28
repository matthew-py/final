import time
from rpg_map import map_of_floors
from rpg_menu import *
from starting_game import *
from rpg_upstairs import *


def basement_options():
    global circuit_breaker_status
    circuit_breaker_status = circuit_breaker.pop(0)
    '''menu for main floor includes list and actions'''
    print("menu:")
# showing where you can go
    print("                     type exit to close")
    print("*area options")
    print("-main floor")
    print("-upstairs master bed room")
    print("-basement")
# telling them what players are on that floor baised off circuit_breaker var
    if circuit_breaker_status == 1:
        print("\n*players nearby")
        print("-Rick")
        print("-Joah")
    else:
        print("\n*players nearby")
        print("-Rick")

# telling them what weapons they currently have
    print("\n*current weapons")
    print("-use gun")
    print("-use poison")


def basement_menu():
    '''takes action for menu baised off whos downstairs'''
    player_location = "main floor"
    while player_location == 'main floor':
        if circuit_breaker_status == 1:
            # taking use input
            action = input("what action would you like to take: ")
# if else chain baised on their input to decide action
            if action == "main floor":
                print("you go up the stairs and through the door")
                time.sleep(5)
                print('\n' * 100)
                menu_options_main()
                main_menu()
            elif action == "upstairs master bed room":
                print("you go up the stairs and through the door")
                time.sleep(5)
                print('\n' * 100)
                upstairs_options()
                upstairs_menu()
            elif action == "basement":
                print("that is your current location")
            elif action == "use gun":
                print("error usage: use gun player_name")
# breaks added for game over to break loop
            elif action == 'use gun rick':
                print("you shot rick but joah noticed and yelled")
                print("game over")
                print("starting new game in 5 seconds")
                time.sleep(5)
                print('\n' * 100)
                game_start()
            elif action == "use gun joah":
                print("you shot joah but rick noticed and yelled")
                print("game over")
                print("starting new game in 5 seconds")
                time.sleep(5)
                print('\n' * 100)
                game_start()
            elif action == "use poison":
                print("error usage use poison player_name")
            elif action == "use poison joah":
                print("print you can only use poison on the target")
            elif action == "use poison rick":
                print("print you can only use poison on\
                      the target when they are alone")
            elif action == "exit":
                print("back")
                break
            else:
                print("error try again")
        else:
                # taking use input
            action = input("what action would you like to take: ")
# if else chain baised on their input to decide action
            if action == "main floor":
                print("you go up the stairs and through the door")
                time.sleep(5)
                print('\n' * 100)
                menu_options_main()
                main_menu()
            elif action == "upstairs master bed room":
                print("you go up the stairs and through the door")
                time.sleep(5)
                print('\n' * 100)
                upstairs_options()
                upstairs_menu()
            elif action == "basement":
                print("that is your current location")
            elif action == "use gun":
                print("error usage: use gun player_name")
# breaks added for game over to break loop
            elif action == 'use gun rick':
                print("you shot rick eveyone heard it but\
                       its to late, your gone never to be seen again")
                print("WIN")
                exit()
            elif action == "use poison":
                print("error usage use poison player_name")
            elif action == "use poison rick":
                print("you slip rick the posion, by the\
                      time they know what happend rick\
                      will be dead and youll be long gone")
                print('WIN')
                exit()
            elif action == "exit":
                print("back")
                break
            else:
                print("error try again")
