"""This is a terminal based chess"""
import json

# loading the json file which i save the game position for each color
with open('white_board.json', 'r' , encoding='utf8') as file:
    white_data = json.load(file)

with open('black_board.json', 'r' , encoding='utf8') as file:
    black_data = json.load(file)

move_counter = 0
move_history = []
total_moves_possible = []
square_to_num = {'a': 1 , 'b' : 2 , 'c' : 3 , 'd' : 4 , 'e' : 5 , 'f' : 6 , 'g' : 7 , 'h' : 8}


# To be implemented...
def castle_possib():
    """If castling is possible or not"""
    pass

def moves_possible(number):
    """
    Input : total moves possible
    Output : what happnes
    """
    if number == 0:
        return "Impossible move!"
    elif number == 1:
        return "Move was made succesfully"
    else:
        return "This feutue is not implemented yet please return later!"

def legal(pieace , first_square , second_square):
    """This function's job is too return true/false if the move is legal or not"""

    base_square_word = square_to_num[first_square[0]]
    base_square_num = int(first_square[1])

    dest_square_word = square_to_num[second_square[0]]
    dest_square_num = int(second_square[1])

    if pieace == 'k':
        if (abs(base_square_num - dest_square_num) == 1) or (abs(base_square_word - dest_square_word) == 1) :
            return True
    elif pieace == 'q':
        if (base_square_word == dest_square_word) or (base_square_num == dest_square_num) or (base_square_word + dest_square_word == base_square_num + dest_square_num) or (base_square_num + base_square_word == dest_square_num + dest_square_word):
            return True
    elif pieace == 'b':
        if (base_square_word + dest_square_word == base_square_num + dest_square_num) or (base_square_num + base_square_word == dest_square_num + dest_square_word):
            return True
    elif pieace == 'n':
        if ( abs(base_square_word - dest_square_word) == 1 and abs(base_square_num - dest_square_num) == 2) or (abs(base_square_word - dest_square_word) == 2 and abs(base_square_num - dest_square_num) == 1):
            return True
    elif pieace == 'r':
        if (base_square_word == dest_square_word) or (base_square_num == dest_square_num):
            return True
    elif pieace =='p':
        if (base_square_num - dest_square_num == -1) and (base_square_word == dest_square_word) and (move_counter % 2 == 0):
            return True
        elif (base_square_num - dest_square_num == 1) and (base_square_word == dest_square_word) and (move_counter % 2 == 1):
            return True
    else:
        return False
    return False

while True:
    move = input().lower().split(" ")
    if move_counter % 2 == 0: 
        # white to move
        for square in white_data:
            # iteration over the white data
            if white_data[square] == move[0]:
                # if a square had the wanted pieace
                if legal(move[0] , square , move[1]):
                    # if the pieace is able to do such a move
                    move_history.append(move)
                    white_data[move[1]] = move[0]
                    white_data[square] = ""
                    move_counter += 1
                    total_moves_possible.append(1)
                    break
                total_moves_possible.append(0)
            else:
                continue
        print(moves_possible(sum(total_moves_possible)))
        total_moves_possible.clear()
        print(white_data)

    else:
        # black to move
        for square in black_data:
            # iteration over the black data
            if black_data[square] == move[0]:
                # if a square had the wanted pieace
                if legal(move[0] , square , move[1]):
                    # if the pieace is able to do such a move
                    move_history.append(move)
                    black_data[move[1]] = move[0]
                    black_data[square] = ""
                    move_counter += 1
                    total_moves_possible.append(1)
                    break
                total_moves_possible.append(0)
            else:
                continue
        print(moves_possible(sum(total_moves_possible)))
        total_moves_possible.clear()
        print(black_data)
