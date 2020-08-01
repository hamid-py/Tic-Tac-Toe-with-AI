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
            print(f'{x_o_matrix[0][0]} wins')
            quit['exit1'] = False
            return True
        elif ''.join(x_o_matrix[2][0]) == ''.join(x_o_matrix[1][1]) == ''.join(x_o_matrix[0][2]) and ''.join(
                x_o_matrix[2][0]) != "_":
            print(f'{x_o_matrix[2][0]} wins')
            quit['exit1'] = False
            return True
        elif all(([j != '_' for i in x_o_matrix for j in i])) and i == 2:
            print('Draw')
            quit['exit1'] = False
            return 'True'


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
            return f'{x} {y}'


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
            if new_x_o_matrix[i][j] == '_':
                empty_spot_list.append(f'{i} {j}')
    return empty_spot_list


def minmax(new_x_o_matrix, depth):
    score_dict = []
    empty_spot = get_empty_spot(new_x_o_matrix)
    for i in empty_spot:
        x = int(i.split()[0])
        y = int(i.split()[1])
        if count_x_o(new_x_o_matrix) == 'X':
            new_x_o_matrix[x][y] = 'X'
            if check_win(new_x_o_matrix) == True:
                new_x_o_matrix[x][y] = '_'
                return {'10': i}
            elif check_win(new_x_o_matrix) == 'True':
                new_x_o_matrix[x][y] = '_'
                return {'0': i}
            else:
                score_dict.append(minmax(new_x_o_matrix, depth + 1))
                new_x_o_matrix[x][y] = '_'

        else:
            new_x_o_matrix[x][y] = 'O'
            if check_win(new_x_o_matrix) == True:
                new_x_o_matrix[x][y] = '_'
                return {'-10': i}
            elif check_win(new_x_o_matrix) == 'True':
                new_x_o_matrix[x][y] = '_'
                return {'0': i}
            else:
                score_dict.append(minmax(new_x_o_matrix, depth + 1))
                new_x_o_matrix[x][y] = '_'

    if score_dict:
        if count_x_o(new_x_o_matrix) == 'X':
            then_list = []
            zero_list = []
            neg_then_list = []
            for i in score_dict:
                if '10' in i:
                    then_list.append(i)
                elif '0' in i:
                    zero_list.append(i)
                else:
                    neg_then_list.append(i)
            if then_list:
                return then_list[0]
            if zero_list:
                return zero_list[0]
            return neg_then_list[0]
        if count_x_o(new_x_o_matrix) == 'O':
            then_list = []
            zero_list = []
            neg_then_list = []
            for i in score_dict:
                if '-10' in i:
                    neg_then_list.append(i)
                if '0' in i:
                    zero_list.append(i)
                else:
                    then_list.append(i)
            if neg_then_list:
                return neg_then_list[0]
            if zero_list:
                return zero_list[0]
            return then_list[0]


def system_difficult_choice(new_x_o_matrix, str_):
    depth = 0
    score_dict = {10: [], -10: [], 0: []}
    empty_spot = get_empty_spot(new_x_o_matrix)
    if len(empty_spot) == 9:
        return system_choice(new_x_o_matrix, 'X')
    else:
        for i in empty_spot:
            x = int(i.split()[0])
            y = int(i.split()[1])
            new_x_o_matrix[x][y] = str_
            if check_win(new_x_o_matrix) == True:
                score_dict[10].append(i)
            elif check_win(new_x_o_matrix) == 'True':
                score_dict[0].append(i)
            else:
                score = minmax(new_x_o_matrix, depth + 1)
                if '10' in score:
                    score_dict[10].append(i)
                elif '-10' in score:
                    score_dict[-10].append(i)
                elif '0' in score:
                    score_dict[0].append(i)

            new_x_o_matrix[x][y] = '_'
        print()
        if score_dict[10]:
            return score_dict[10][0]
        if score_dict[0]:
            return score_dict[0][0]
        return score_dict[-10][0]


def system_very_difficult(new_x_o_matrix, str_):
    x_y = system_difficult_choice(new_x_o_matrix, str_).split()
    x = int(x_y[0])
    y = int(x_y[1])
    print('Making move level "hard"')
    new_x_o_matrix[x][y] = str_
    quit['exit1'] = True


quit = {'exit': True, 'exit1': True}
x_o_list = ()
while quit['exit']:
    quit['exit1'] = True
    x_o_matrix = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    what_to_do = input()
    if what_to_do == 'exit':
        quit['exit'] = False
        continue
    elif what_to_do == 'start hard user':
        prin_x_o(x_o_matrix)
        while quit['exit1']:
            system_very_difficult(x_o_matrix, 'X')
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
                    system_very_difficult(x_o_matrix, 'O')
                    prin_x_o(x_o_matrix)
                    check_win(x_o_matrix)

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
