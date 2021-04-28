from rpg_menu import *
from starting_game import *
circuit_breaker = [1, 2]


def upstairs_options():
    '''menu for upstairs includes list and actions'''
    print("menu:")
# showing where you can go
    print("                     type exit to close")
    print("*area options")
    print("-main floor")
    print("-upstairs master bed room")
    print("-basement")
# telling them what players are on that floor
    print("\n*players nearby")
    print("-taylea")
# telling them what weapons they currently have
    print("\n*current weapons")
    print("-use gun")
    print("-use poison")
    print('\n flip circuit breaker?')


def upstairs_menu():
    import time
    from rpg_map import map_of_floors
    from rpg_basement import basement_options
    from rpg_basement import basement_menu
    '''takes action for menu'''
    player_location = "upstairs"
    while player_location == 'upstairs':
        # taking use input
        action = input("what action would you like to take: ")
# if else chain baised on their input to decide action
        if action == "main floor":
            print("you walk down the stairs")
            print('\n' * 100)
            menu_options_main()
            main_menu()
        elif action == "upstairs master bed room":
            print("that is your current location")
        elif action == "basement":
            print("you go down the stairs and through the door")
            time.sleep(5)
            basement_options()
            basement_menu()
        elif action == "use gun":
            print("error usage: use gun player_name")
# breaks added for game over to break loop
        elif action == "use gun taylea":
            print("you shot taylea but everyone noticed")
            print("game over")
            print("starting new game in 5 seconds")
            time.sleep(5)
            print('\n' * 100)
            game_start()
        elif action == "use poison":
            print("error usage use poison player_name")
        elif action == "use poison taylea":
            print("you can only use poison on the target")
        elif action == 'flip circuit breaker':
            circuit_breaker.pop(0)
            print("circuit_breaker flipped, joah will come check on it")
            time.sleep(4)
            upstairs_options()
        elif action == "exit":
            print("back")
            break
        else:
            print("error try again")
