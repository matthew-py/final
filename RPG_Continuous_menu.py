# Matthew Deyenberg
# computer science 30 period 1
# 2021/04/01
# simple rpg menu
# setting player to main floor as starting level
player_location = "main floor"


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
    while player_location == 'main floor':
        # taking use input
        action = input("what action would you like to take: ")
# if else chain baised on their input to decide action
        if action == "main floor":
            print("your already on the main floor")
        elif action == "upstairs master bed room":
            print("you go up the stairs and through the door")
        elif action == "basement":
            print("you go down the stairs and through the door")
        elif action == "use gun":
            print("error usage: use gun player_name")
# breaks added for game over to break loop
        elif action == 'use gun josh':
            print("you shot josh but luke noticed and yelled")
            print("game over")
            break
        elif action == "use gun luke":
            print("you shot luke but josh noticed and yelled")
            print("game over")
            break
        elif action == "use poison":
            print("error usage use poison player_name")
        elif action == "use poison josh":
            print("you can only use poison on the target")
        elif action == "use poison luke":
            print("print you can only use poison on the target")
        elif action == "exit":
            break
        else:
            print("error try again")
# calling functions
menu_options_main()
main_menu()
