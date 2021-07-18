import os
import random

clicked = True  # user's turn
count = 0
winner = 0
symbol = ['X', 'O']
list1 = [" ", "|", " ", "|", " "]
list2 = [" ", "|", " ", "|", " "]
list3 = [" ", "|", " ", "|", " "]
existing_locations = []
a = [list1, list2, list3]
location = range(1, 10)


def game_winner():
    global winner
    if not winner:
        if a[0][0] == "O" and a[0][2] == "O" and a[0][4] == 'O':
            print("User2 wins!!!!!")
            winner = True
        elif a[1][0] == "O" and a[1][2] == "O" and a[1][4] == 'O':
            print("User2 wins!!!!!")
            winner = True
        elif a[2][0] == "O" and a[2][2] == "O" and a[2][4] == 'O':
            print("User2 wins!!!!!")
            winner = True

        elif a[0][0] == "O" and a[1][0] == "O" and a[2][0] == 'O':
            print("User2 wins!!!!!")
            winner = True
        elif a[0][1] == "O" and a[1][1] == "O" and a[2][1] == 'O':
            print("User2 wins!!!!!")
            winner = True
        elif a[0][2] == "O" and a[1][2] == "O" and a[2][2] == 'O':
            print("User2 wins!!!!!")
            winner = True

        elif a[0][0] == "O" and a[1][2] == "O" and a[2][4] == 'O':
            print("User2 wins!!!!!")
            winner = True
        elif a[0][4] == "O" and a[1][2] == "O" and a[2][0] == 'O':
            print("User2 wins!!!!!")
            winner = True

        elif a[0][0] == "X" and a[0][2] == "X" and a[0][4] == 'X':
            print("User1 wins!!!!!")
            winner = True
        elif a[1][0] == "X" and a[1][2] == "X" and a[1][4] == 'X':
            print("User1 wins!!!!!")
            winner = True
        elif a[2][0] == "X" and a[2][2] == "X" and a[2][4] == 'X':
            print("User1 wins!!!!!")
            winner = True

        elif a[0][0] == "X" and a[1][0] == "X" and a[2][0] == 'X':
            print("User1 wins!!!!!")
            winner = True
        elif a[0][2] == "X" and a[1][2] == "X" and a[2][2] == 'X':
            print("User1 wins!!!!!")
            winner = True
        elif a[2][4] == "X" and a[1][4] == "X" and a[0][4] == 'X':
            print("User1 wins!!!!!")
            winner = True

        elif a[0][0] == "X" and a[1][2] == "X" and a[2][4] == 'X':
            print("User1 wins!!!!!")
            winner = True
        elif a[0][4] == "X" and a[1][2] == "X" and a[2][0] == 'X':
            print("User1 wins!!!!!")
            winner = True
        elif count == 8:
            print("It's a draw!!!!")
            winner = True


def show():
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print(" ")
        print("---------")


print("New game 🎰🎲")
show()


def make_moves(x, symbol_):
    global count

    if (a[0][0] != "O" or a[0][0] != "X") and x == 1:
        a[0][0] = symbol_
    elif (a[0][2] != "O" or a[0][2] != "X") and x == 2:
        a[0][2] = symbol_
    elif (a[0][4] != "O" or a[0][4] != "X") and x == 3:
        a[0][4] = symbol_
    elif (a[1][0] != "O" or a[1][0] != "X") and x == 4:
        a[1][0] = symbol_
    elif (a[1][2] != "O" or a[1][2] != "X") and x == 5:
        a[1][2] = symbol_
    elif (a[1][4] != "O" or a[1][4] != "X") and x == 6:
        a[1][4] = symbol_
    elif (a[2][0] != "O" or a[2][0] != "X") and x == 7:
        a[2][0] = symbol_
    elif (a[2][2] != "O" or a[2][2] != "X") and x == 8:
        a[2][2] = symbol_
    elif (a[2][4] != "O" or a[2][4] != "X") and x == 9:
        a[2][4] = symbol_
    game_winner()


# def clear():
#     if os.name == 'posix':
#         _ = os.system('clear')
#     else:
#         _= os.system('cls')
#     print('cleared screen')

while not winner and count < 9:

    if clicked:
        position = int(input('User1 enter position:'))
        print('User1 chooses:', position)
        if position not in existing_locations:
            existing_locations.append(position)
            make_moves(position, symbol[0])
            clicked = False
            count += 1
        else:
            print('WARNING ---> User1 position already filled,choose another position')
    else:
        # position = random.choice(location)
        position = int(input('User2 enter position:'))
        print('User2 chooses:', position)
        if position not in existing_locations:
            existing_locations.append(position)

            make_moves(position, symbol[1])
            clicked = True
            count += 1

        else:
            print('WARNING ---> User2 position already filled,choose another position')
    print("Current game 🎰🎲")
    show()

    if winner:
        response = input("Do you want to play again(Yes/No)").title()
        if response == 'Yes':
            # clear()
            winner = False
            count = 0
            clicked = True
            symbol = ['X', 'O']
            list1 = [" ", "|", " ", "|", " "]
            list2 = [" ", "|", " ", "|", " "]
            list3 = [" ", "|", " ", "|", " "]
            existing_locations = []
            a = [list1, list2, list3]
            location = range(1, 10)
            print("New game 🎰🎲")
            show()

else:
    print('GoodBye!!!!!!!')
