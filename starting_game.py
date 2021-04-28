def game_start():
    '''starts main game'''
    from rpg_basement import basement_options
    from rpg_basement import basement_menu
    from rpg_map import map_of_floors
    from rpg_menu import menu_options_main
    from rpg_menu import main_menu
    player_location = "main floor"
    player = []
    player = input('Whats your name: ')
    items = {'gun': {'bullets': "8"}, 'poison': '1'}
    people = {'josh': 'bystander', 'luke': 'bystander',
              'rick': 'target', 'joah': 'bystander',
              'taylea': 'bystander', player: 'assassin'}
    rooms = {'main floor': ['josh', 'luke'],
             'upstairs master bed room': 'taylea',
             'basement': ['rick', 'joah']}
# setting varable for loops
    x = 0
# showing the player whats avalible
    print("People at the party:")
    for players, tags in people.items():
        x = x + 1
        print(str(x)+'.', players, ':', tags)
# resetting x and printing
    x = 0
    print("Items")
    for item, info in items.items():
        x = x + 1
        print(str(x)+'.', item, info)
# resetting x again and printing
    x = 0
    print("Rooms")
    for room, bystanders in rooms.items():
        x = x + 1
        print(str(x)+'.', room, ":", bystanders)
# calls current functions
    while player_location == "main floor":
        choice = input("map, menu or quit?:     ")
        if choice == 'map':
            map_of_floors()
        if choice == 'menu':
            print('\n' * 100)
            menu_options_main()
            main_menu()
        if choice == 'quit':
            exit()
