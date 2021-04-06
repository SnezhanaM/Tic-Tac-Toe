cells = ('_________')
cell = list(cells)

def field_input():
    print('''---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------'''.format(*cell[0:9]))

def coordinate_input_X():
    #List of all possbile coordinates to compare user input against
    coordinates = ["1 3", "2 3", "3 3", "1 2", "2 2", "3 2", "1 1", "2 1", "3 1"]
    user_turn = input('Enter the coordinates: ')

    if user_turn.replace(' ','').isdecimal() == False:
        print("You should enter numbers!")
        coordinate_input_X() #recalled function so it would start again
    elif user_turn not in coordinates:
        print("Coordinates should be from 1 to 3!")
        coordinate_input_X()
    elif cell[coordinates.index(user_turn)] != "_":
        print("This cell is occupied! Choose another one!")
        coordinate_input_X()
    elif user_turn in coordinates:
        del cell[coordinates.index(user_turn)]
        cell.insert(coordinates.index(user_turn), "X")

def coordinate_input_O():
    coordinates = ["1 3", "2 3", "3 3", "1 2", "2 2", "3 2", "1 1", "2 1", "3 1"]
    user_turn = input('Enter the coordinates: ')

    if user_turn.replace(' ', '').isdecimal() == False:
        print("You should enter numbers!")
        coordinate_input_O()  # recalled function so it would start again
    elif user_turn not in coordinates:
        print("Coordinates should be from 1 to 3!")
        coordinate_input_O()
    elif cell[coordinates.index(user_turn)] != "_":
        print("This cell is occupied! Choose another one!")
        coordinate_input_O()
    elif user_turn in coordinates:
        del cell[coordinates.index(user_turn)]
        cell.insert(coordinates.index(user_turn), "O")

def isWinner(input, el):
    return ((input[0] == el and input[1] == el and input[2] == el) or  # across the top
            (input[3] == el and input[4] == el and input[5] == el) or  # across the middle
            (input[6] == el and input[7] == el and input[8] == el) or  # across the bottom
            (input[0] == el and input[3] == el and input[6] == el) or  # down the left side
            (input[1] == el and input[4] == el and input[7] == el) or  # down the middle
            (input[2] == el and input[5] == el and input[8] == el) or  # down the right side
            (input[0] == el and input[4] == el and input[8] == el) or  # diagonal
            (input[2] == el and input[4] == el and input[6] == el))  # diagonal

def check_winner():
    o_num = 0
    x_num = 0
    for i in range(0, 9):
        if cell[i] == "X":
            x_num += 1
        if cell[i] == "O":
            o_num += 1
    if isWinner(cell, 'X') and isWinner(cell, 'O') or not isWinner(cell, 'X') and not isWinner(cell, 'O') and abs(x_num - o_num) >= 2:
        return "Impossible"
    elif isWinner(cell, 'X') and not isWinner(cell, 'O'):
        return "X wins"
    elif isWinner(cell, 'O') and not isWinner(cell, 'X'):
        return "O wins"
    elif "_" not in cell:
        return "Draw"
    elif not isWinner(cell, 'X') or not isWinner(cell, 'O'):
        if "_" in cell:
            pass


field_input()
while True:
    coordinate_input_X()
    field_input()
    if check_winner() == 'X wins' or check_winner() == "Draw" or check_winner() == "Impossible":
        print(check_winner())
        break
    coordinate_input_O()
    field_input()
    if check_winner() == "O wins" or check_winner() == "Draw" or check_winner() == "Impossible":
        print(check_winner())
        break
