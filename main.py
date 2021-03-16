# Matthew Deyenberg
# computer science 30 period 1
# 2021/03/16
# rpg inventory
# setting player name and making/showing lists
player = []
player = input('Whats your name: ')
items = ['gun', 'poison']
people = ['josh', 'luke', 'rick', 'joah', 'taylea', player]
rooms = ['main floor', 'upstairs master bed room', 'basement']
# setting varable for loops
x = 0
# showing the player whats avalible
print("People at the party:")
for players in people:
    x = x + 1
    print(str(x)+'.', players)
# resetting x and printing
x = 0
print("Items")
for item in items:
    x = x + 1
    print(str(x)+'.', item)
# resetting x again and printing
x = 0
print("Rooms")
for room in rooms:
    x = x + 1
    print(str(x)+'.', room)
