import copy
import random


def count_x_o(x_o_matrix):
    x_cell = [i for i in x_o_matrix for j in i if j == 'X']
    y_cell = [i for i in x_o_matrix for j in i if j == 'O']
    if len(x_cell) > len(y_cell):
        return 'O'
    return 'X'


def check_correct_x_o(coordinates):
    coordinates_numeric = all(map(lambda x: x.isnumeric(), coordinates))
    if coordinates_numeric:
        coordinates_right_number = all(map(lambda x: 0 < int(x) < 4, coordinates))
        if coordinates_right_number:
            return True
        else:
            print('Coordinates should be from 1 to 3!')
    else:
        print('You should enter numbers!')


def occupied_check(x, y, matrix_list):
    if matrix_list[x - 1][y - 1] != '_':
        print('This cell is occupied! Choose another one!')
        return False
    else:
        return True


def check_win(x_o_matrix):
    for i in range(3):
        if ''.join(x_o_matrix[i][0]) == ''.join(x_o_matrix[i][1]) == ''.join(x_o_matrix[i][2]) and "_" not in \
                x_o_matrix[i]:
            # prin_x_o(x_o_matrix)
            print(f'{x_o_matrix[i][0]} wins')
            quit['exit1'] = False
            return True
        elif ''.join(x_o_matrix[0][i]) == ''.join(x_o_matrix[1][i]) == ''.join(x_o_matrix[2][i]) and ''.join(
                x_o_matrix[0][i]) != "_":
            # prin_x_o(x_o_matrix)
            print(f'{x_o_matrix[0][i]} wins')
            quit['exit1'] = False
            return True
        elif ''.join(x_o_matrix[0][0]) == ''.join(x_o_matrix[1][1]) == ''.join(x_o_matrix[2][2]) and ''.join(
                x_o_matrix[0][0]) != "_":
            # prin_x_o(x_o_matrix)
            print(f'{x_o_matrix[0][0]} wins')
            quit['exit1'] = False
            return True
        elif ''.join(x_o_matrix[2][0]) == ''.join(x_o_matrix[1][1]) == ''.join(x_o_matrix[0][2]) and ''.join(
                x_o_matrix[2][0]) != "_":
            # prin_x_o(x_o_matrix)
            print(f'{x_o_matrix[2][0]} wins')
            quit['exit1'] = False
            return True
        elif all(([j != '_' for i in x_o_matrix for j in i])) and i == 2:
            # prin_x_o(x_o_matrix)
            print('Draw')
            quit['exit1'] = False
            return 'True'
        # elif i == 2:
        #     prin_x_o(x_o_matrix)
        #     print('Game not finished')


def prin_x_o(x_o_matrix):
    print('-' * 9)
    print(f'| {(" ".join(x_o_matrix[2])).replace("_", " ")} |', f'| {" ".join(x_o_matrix[1]).replace("_", " ")} |',
          f'| {" ".join(x_o_matrix[0]).replace("_", " ")} |', sep='\n')
    print('-' * 9)


def system_choice(x_o_matrix, str):
    while True:
        x = random.choice([0, 1, 2])
        y = random.choice([0, 1, 2])
        if x_o_matrix[x][y] == '_':
            x_o_matrix[x][y] = str
            print('Making move level "easy"')
            break


def player_choice(x_o_matrix):
    coordinates = input('Enter the coordinates: ').split()
    if check_correct_x_o(coordinates):
        x_y = [int(i) for i in coordinates]
        if len(x_y) == 2:
            x = x_y[1]
            y = x_y[0]
            if occupied_check(x, y, x_o_matrix):
                cell = count_x_o(x_o_matrix)
                x_o_matrix[x - 1][y - 1] = cell
                return True
            else:
                return False


def system_medium_choice(x_o_matrix, str_, opp_str):
    column_x_o = [[x_o_matrix[0][0], x_o_matrix[1][0], x_o_matrix[2][0]],
                  [x_o_matrix[0][1], x_o_matrix[1][1], x_o_matrix[2][1]],
                  [x_o_matrix[0][2], x_o_matrix[1][2], x_o_matrix[1][2]]]
    diameter_x_o = [[x_o_matrix[0][0], x_o_matrix[1][1], x_o_matrix[2][2]],
                    [x_o_matrix[2][0], x_o_matrix[1][1], x_o_matrix[0][2]]]
    for i in range(len(x_o_matrix)):
        if str_ not in x_o_matrix[i] and x_o_matrix[i].count(opp_str) == 2:
            x_o_matrix[i] = (' '.join(x_o_matrix[i])).replace('_', str_).split()
            print('Making move level "medium"')
            return True
    for i in range(len(column_x_o)):
        if str_ not in column_x_o[i] and column_x_o[i].count(opp_str) == 2:
            for j in range(3):
                if x_o_matrix[j][i] == '_':
                    x_o_matrix[j][i] = str_
                    print('Making move level "medium"')
            return True
    for i in range(len(diameter_x_o)):
        if str_ not in diameter_x_o[i] and diameter_x_o[i].count(opp_str) == 2:
            for j in range(3):
                if diameter_x_o[i][j] == '_':
                    if i == 0:
                        x_o_matrix[j][j] = str_
                        print('Making move level "medium"')
                    else:
                        if j == 0:
                            x_o_matrix[2][0] = str_
                        elif j == 1:
                            x_o_matrix[1][1] = str_
                        elif j == 2:
                            x_o_matrix[2][0] = str_
                        print('Making move level "medium"')

            return True

    while True:
        x = random.choice([0, 1, 2])
        y = random.choice([0, 1, 2])
        if x_o_matrix[x][y] == '_':
            x_o_matrix[x][y] = str_
            print('Making move level "medium"')
            return True


def get_empty_spot(x_o_list):
    empty_spot_list = []
    new_x_o_matrix = x_o_list.copy()
    for i in range(3):
        for j in range(3):
            print(new_x_o_matrix[i][j], 'new_x_o_matrix[i][j]', i, j)
            if new_x_o_matrix[i][j] == '_':
                empty_spot_list.append(f'{i} {j}')
    print(empty_spot_list, 'empty matrix')

    return empty_spot_list


def system_difficult_choice(new_x_o_matrix):
    other_spot_dict = {}
    score_list = []
    # print(x_o_matrix == new_x_o_matrix)
    score_spot_dict = dict()
    print(new_x_o_matrix, del_list, 'new list and old list')
    empty_spot_list = get_empty_spot(new_x_o_matrix)
    if len(empty_spot_list) == 0:
        return 0
    else:
        for i in empty_spot_list:
            x = int(i.split()[0])
            y = int(i.split()[1])
            if count_x_o(new_x_o_matrix) == 'X':
                print('x starts', i)
                new_x_o_matrix[x][y] = count_x_o(new_x_o_matrix)
                if check_win(new_x_o_matrix) == True:
                    print('x wins')
                    score_spot_dict[10] = i
                    return score_spot_dict
                elif check_win(new_x_o_matrix) == 'True':
                    print('x draw')
                    score_spot_dict[0] = i
                    return score_spot_dict
                else:
                    print('khoesho seda zad ', i)
                    score_list.append(system_difficult_choice(new_x_o_matrix))
            else:
                print('O starts', i)
                new_x_o_matrix[x][y] = count_x_o(new_x_o_matrix)
                if check_win(new_x_o_matrix) == True:
                    print('O wins')
                    score_spot_dict[-10] = i
                    return score_spot_dict
                elif check_win(new_x_o_matrix) == 'True':
                    print("O draw")
                    score_spot_dict[0] = i
                    return score_spot_dict
                else:
                    print("o khodesh sada za", i)
                    score_list.append(system_difficult_choice(new_x_o_matrix))
del_list = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
new_matrix = del_list.copy()

quit = {'exit': True, 'exit1': True}
x_o_list = ()
while quit['exit']:
    quit['exit1'] = True
    x_o_matrix = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    new_matrix = x_o_matrix.copy()
    what_to_do = input()
    if what_to_do == 'exit':
        quit['exit'] = False
        continue
    elif what_to_do == 'start easy medium':
        prin_x_o(x_o_matrix)
        while quit['exit1']:
            system_choice(x_o_matrix, 'X')
            prin_x_o(x_o_matrix)
            if not check_win(x_o_matrix):
                system_medium_choice(x_o_matrix, 'O', 'X')
                prin_x_o(x_o_matrix)
                check_win(x_o_matrix)
    elif what_to_do == 'start medium easy':
        prin_x_o(x_o_matrix)
        while quit['exit1']:
            system_medium_choice(x_o_matrix, 'X', 'O')
            prin_x_o(x_o_matrix)
            if not check_win(x_o_matrix):
                system_choice(x_o_matrix, 'O')
                prin_x_o(x_o_matrix)
                check_win(x_o_matrix)
    elif what_to_do == 'start medium medium':
        prin_x_o(x_o_matrix)
        while quit['exit1']:
            system_medium_choice(x_o_matrix, 'X', 'O')
            prin_x_o(x_o_matrix)
            if not check_win(x_o_matrix):
                system_medium_choice(x_o_matrix, 'O', 'X')
                prin_x_o(x_o_matrix)
                check_win(x_o_matrix)
                
    elif what_to_do == 'start medium user':
        prin_x_o(x_o_matrix)
        while quit['exit1']:
            system_medium_choice(x_o_matrix, 'X', 'O')
            prin_x_o(x_o_matrix)
            if not check_win(x_o_matrix):
                while not player_choice(x_o_matrix):
                    continue
                prin_x_o(x_o_matrix)

    elif what_to_do == 'start user medium':
        prin_x_o(x_o_matrix)
        while quit['exit1']:
            if player_choice(x_o_matrix):
                prin_x_o(x_o_matrix)
                if not check_win(x_o_matrix):
                    system_medium_choice(x_o_matrix, 'O', 'X')
                    prin_x_o(x_o_matrix)
                    check_win(x_o_matrix)

    elif what_to_do == 'start easy easy':
        prin_x_o(x_o_matrix)
        while quit['exit1']:
            system_choice(x_o_matrix, 'X')
            prin_x_o(x_o_matrix)
            if not check_win(x_o_matrix):
                system_choice(x_o_matrix, 'O')
                prin_x_o(x_o_matrix)
                check_win(x_o_matrix)
    elif what_to_do == 'start easy user':
        prin_x_o(x_o_matrix)
        while quit['exit1']:
            system_choice(x_o_matrix, 'X')
            prin_x_o(x_o_matrix)
            if not check_win(x_o_matrix):
                while not player_choice(x_o_matrix):
                    continue
                prin_x_o(x_o_matrix)

    elif what_to_do == 'start user easy':
        prin_x_o(x_o_matrix)
        while quit['exit1']:
            if player_choice(x_o_matrix):
                prin_x_o(x_o_matrix)
                if not check_win(x_o_matrix):
                    system_choice(x_o_matrix, 'O')
                    prin_x_o(x_o_matrix)
                    check_win(x_o_matrix)
    elif what_to_do == 'start user user':
        prin_x_o(x_o_matrix)
        while quit['exit1']:
            if player_choice(x_o_matrix):
                prin_x_o(x_o_matrix)
                if not check_win(x_o_matrix):
                    while not player_choice(x_o_matrix):
                        continue
                    prin_x_o(x_o_matrix)
    elif what_to_do == 'start hard user':
        prin_x_o(x_o_matrix)
        while quit['exit1']:
            system_medium_choice(x_o_matrix, 'X', 'O')
            prin_x_o(x_o_matrix)
            if not check_win(x_o_matrix):
                while not player_choice(x_o_matrix):
                    continue
                prin_x_o(x_o_matrix)
        
    elif what_to_do == 'start user hard':
        prin_x_o(x_o_matrix)
        while quit['exit1']:
            if player_choice(x_o_matrix):
                prin_x_o(x_o_matrix)
                if not check_win(x_o_matrix):
                    system_medium_choice(x_o_matrix, 'O', 'X')
                    prin_x_o(x_o_matrix)
                    check_win(x_o_matrix)
    elif what_to_do == 'start hard hard':
        prin_x_o(x_o_matrix)
        while quit['exit1']:
            system_medium_choice(x_o_matrix, 'X', 'O')
            prin_x_o(x_o_matrix)
            if not check_win(x_o_matrix):
                system_medium_choice(x_o_matrix, 'O', 'X')
                prin_x_o(x_o_matrix)
                check_win(x_o_matrix)
    
    elif what_to_do == 'start medium hard':
        prin_x_o(x_o_matrix)
        while quit['exit1']:
            system_medium_choice(x_o_matrix, 'X', 'O')
            prin_x_o(x_o_matrix)
            if not check_win(x_o_matrix):
                system_medium_choice(x_o_matrix, 'O', 'X')
                prin_x_o(x_o_matrix)
                check_win(x_o_matrix)
    elif what_to_do == 'start hard medium':
        prin_x_o(x_o_matrix)
        while quit['exit1']:
            system_medium_choice(x_o_matrix, 'X', 'O')
            prin_x_o(x_o_matrix)
            if not check_win(x_o_matrix):
                system_medium_choice(x_o_matrix, 'O', 'X')
                prin_x_o(x_o_matrix)
                check_win(x_o_matrix)
    elif what_to_do == 'start easy hard':
        prin_x_o(x_o_matrix)
        while quit['exit1']:
            system_medium_choice(x_o_matrix, 'X', 'O')
            prin_x_o(x_o_matrix)
            if not check_win(x_o_matrix):
                system_medium_choice(x_o_matrix, 'O', 'X')
                prin_x_o(x_o_matrix)
                check_win(x_o_matrix)
    elif what_to_do == 'start hard easy':
        prin_x_o(x_o_matrix)
        while quit['exit1']:
            system_medium_choice(x_o_matrix, 'X', 'O')
            prin_x_o(x_o_matrix)
            if not check_win(x_o_matrix):
                system_medium_choice(x_o_matrix, 'O', 'X')
                prin_x_o(x_o_matrix)
                check_win(x_o_matrix)




    else:
        print('Bad parameters!')
