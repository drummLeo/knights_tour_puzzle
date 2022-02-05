def get_dimensions(input_, input_string="Enter your next move: ", x_limit=99, y_limit=99):
    try:
        input_list = input_.split()
        dimension = [int(input_list[0]), int(input_list[1])]
    except IndexError:
        print("Invalid dimensions!")
        print()
        return get_dimensions(input_=input(input_string), input_string=input_string,
                              x_limit=x_limit, y_limit=y_limit)
    except ValueError:
        print("Invalid dimensions!")
        print()
        return get_dimensions(input_=input(input_string), input_string=input_string,
                              x_limit=x_limit, y_limit=y_limit)
    else:
        if dimension[0] < 1 or dimension[1] < 1:
            print("Invalid dimensions!")
            print()
            return get_dimensions(input_=input(input_string), input_string=input_string,
                                  x_limit=x_limit, y_limit=y_limit)
        if dimension[0] > x_limit or dimension[1] > y_limit:
            print("Invalid dimensions!")
            print()
            return get_dimensions(input_=input(input_string), input_string=input_string,
                                  x_limit=x_limit, y_limit=y_limit)

        return [dimension[0], dimension[1]]


x = 0
y = 0


def make_chessboard(dimensions=get_dimensions(input_=input("Enter your board dimensions: "),
                                              input_string="Enter your board dimensions: ")):
    global x
    global y

    x = dimensions[0]
    y = dimensions[1]

    cell_width_ = 1
    if x * y >= 9:
        cell_width_ = 2
    if x * y >= 81:
        cell_width_ = 3

    chessboard_ = []

    numerator = "  "
    if y + 1 >= 10:
        numerator = ' ' + numerator

    for j in range(1, x + 1):
        numerator += cell_width_ * ' ' + str(j)
    if cell_width_ == 3:
        numerator = numerator[1:]

    for i in range(1, y + 1):
        row_ = f"{i}|" + (x * f" {cell_width_ * '_'}") + ' |'
        if y >= 10:
            if i < 10:
                row_ = ' ' + row_
        chessboard_.append(row_)

    border = (y // 10 + 1) * ' ' + (3 + (cell_width_ + 1) * x) * '-'
    chessboard_.insert(0, border)
    chessboard_.append(border)

    chessboard_ = chessboard_[::-1]
    chessboard_.append(numerator)

    return [chessboard_, cell_width_]


def get_game_mode():
    try_puzzle_input = input("Do you want to try the puzzle? (y/n): ")
    if try_puzzle_input == 'y':
        return False
    elif try_puzzle_input == 'n':
        return True
    else:
        print("Invalid input!")
        return get_game_mode()


def rewrite(pos_x, pos_y, board_, cw, inp):
    if len(board_) >= 13:
        pos_x += 1
    aux_board = board_
    temp = board_[pos_y]
    temp = temp[:pos_x] + (cw - len(str(inp))) * ' ' + str(inp) + temp[pos_x + cw:]
    if cw // 3 == 1:
        temp = temp[:len(temp) - 1] + '|'
    aux_board.remove(board_[pos_y])
    aux_board.insert(pos_y, temp)
    return aux_board


def print_board(board_):
    for row_ in board_:
        print(row_)


solutions = []


def solution(x__, y__, cb, cw, tm=1):
    def is_sol():
        nonlocal cb
        for i in cb:
            if i.count("_") > 2 * cw:
                print(f"Failed: {tm}")
                print_board(cb)
                return False

        global solutions
        if len(solutions) == 0:
            for c in cb:
                solutions.append(c)
        return True

    pp = get_possible_moves(x__, y__, cb, cw, get_move=True)
    try:
        bp = pp[0]
    except IndexError:
        return is_sol
    bps = []
    for p in pp:
        if get_possible_moves(p[0], p[1], cb, cw) < get_possible_moves(bp[0], bp[1], cb, cw):
            bp = p
    for ps in pp:
        if get_possible_moves(ps[0], ps[1], cb, cw) == get_possible_moves(bp[0], bp[1], cb, cw):
            bps.append(ps)

    try:
        mv = bps[0]
    except IndexError:
        return is_sol()
    if get_possible_moves(mv[0], mv[1], cb, cw) == 0:
        return is_sol()
    if len(bps) > 0 and solution(bps[0][0], bps[0][1], rewrite(bps[0][0], bps[0][1], cb, cw, tm), cw, tm + 1):
        mv = bps[0]
    if len(bps) > 1 and solution(bps[1][0], bps[1][1], rewrite(bps[1][0], bps[1][1], cb, cw, tm), cw, tm + 1):
        mv = bps[1]
    if len(bps) > 2 and solution(bps[2][0], bps[2][1], rewrite(bps[2][0], bps[2][1], cb, cw, tm), cw, tm + 1):
        mv = bps[2]
    if len(bps) > 3 and solution(bps[3][0], bps[3][1], rewrite(bps[3][0], bps[3][1], cb, cw, tm), cw, tm + 1):
        mv = bps[3]
    if len(bps) > 4 and solution(bps[4][0], bps[4][1], rewrite(bps[4][0], bps[4][1], cb, cw, tm), cw, tm + 1):
        mv = bps[4]
    if len(bps) > 5 and solution(bps[5][0], bps[5][1], rewrite(bps[5][0], bps[5][1], cb, cw, tm), cw, tm + 1):
        mv = bps[5]
    if len(bps) > 6 and solution(bps[6][0], bps[6][1], rewrite(bps[6][0], bps[6][1], cb, cw, tm), cw, tm + 1):
        mv = bps[6]
    if len(bps) > 7 and solution(bps[7][0], bps[7][1], rewrite(bps[7][0], bps[7][1], cb, cw, tm), cw, tm + 1):
        mv = bps[7]
    if len(bps) > 8 and solution(bps[8][0], bps[8][1], rewrite(bps[8][0], bps[8][1], cb, cw, tm), cw, tm + 1):
        mv = bps[8]
    return solution(mv[0], mv[1], rewrite(mv[0], mv[1], cb, cw, tm), cw, tm + 1)


def get_possible_moves(pos_x, pos_y, cb, cw, debug=False, get_move=False):
    move_count = 0

    top_left_ = [pos_x - 1 * (cw + 1), pos_y - 2]
    top_right_ = [pos_x + 1 * (cw + 1), pos_y - 2]
    left_top_ = [pos_x - 2 * (cw + 1), pos_y - 1]
    left_bottom_ = [pos_x - 2 * (cw + 1), pos_y + 1]
    right_top_ = [pos_x + 2 * (cw + 1), pos_y - 1]
    right_bottom_ = [pos_x + 2 * (cw + 1), pos_y + 1]
    bottom_left_ = [pos_x - 1 * (cw + 1), pos_y + 2]
    bottom_right_ = [pos_x + 1 * (cw + 1), pos_y + 2]
    if debug:
        for h in cb:
            print(h)

        try:
            print('top_left_:')
            print(cb[top_left_[1]][top_left_[0]])
            print('top_right_:')
            print(cb[top_right_[1]][top_right_[0]])
            print('left_top_:')
            print(cb[left_top_[1]][left_top_[0]])
            print('left_bottom_:')
            print(cb[left_bottom_[1]][left_bottom_[0]])
            print('right_top_:')
            print(cb[right_top_[1]][right_top_[0]])
            print('right_bottom_:')
            print(cb[right_bottom_[1]][right_bottom_[0]])
            print('bottom_left_:')
            print(cb[bottom_left_[1]][bottom_left_[0]])
            print('bottom_right_:')
            print(cb[bottom_right_[1]][bottom_right_[0]])
        except IndexError:
            print("Exception")

    moves = []

    if 3 < top_left_[0] < len(cb[0]) - 2 and 0 < top_left_[1] < len(cb) - 2 \
            and cb[top_left_[1]][top_left_[0]] == '_':
        move_count += 1
        moves.append(top_left_)

    if 3 < top_right_[0] < len(cb[0]) - 2 and 0 < top_right_[1] < len(cb) - 2 \
            and cb[top_right_[1]][top_right_[0]] == '_':
        move_count += 1
        moves.append(top_right_)

    if 3 < left_top_[0] < len(cb[0]) - 2 and 0 < left_top_[1] < len(cb) - 2 \
            and cb[left_top_[1]][left_top_[0]] == '_':
        move_count += 1
        moves.append(left_top_)

    if 3 < left_bottom_[0] < len(cb[0]) - 2 and 0 < left_bottom_[1] < len(cb) - 2 \
            and cb[left_bottom_[1]][left_bottom_[0]] == '_':
        move_count += 1
        moves.append(left_bottom_)

    if 3 < right_top_[0] < len(cb[0]) - 2 and 0 < right_top_[1] < len(cb) - 2 \
            and cb[right_top_[1]][right_top_[0]] == '_':
        move_count += 1
        moves.append(right_top_)

    if 3 < right_bottom_[0] < len(cb[0]) - 2 and 0 < right_bottom_[1] < len(cb) - 2 \
            and cb[right_bottom_[1]][right_bottom_[0]] == '_':
        move_count += 1
        moves.append(right_bottom_)

    if 3 < bottom_left_[0] < len(cb[0]) - 2 and 0 < bottom_left_[1] < len(cb) - 2 \
            and cb[bottom_left_[1]][bottom_left_[0]] == '_':
        move_count += 1
        moves.append(bottom_left_)

    if 3 < bottom_right_[0] < len(cb[0]) - 2 and 0 < bottom_right_[1] < len(cb) - 2 \
            and cb[bottom_right_[1]][bottom_right_[0]] == '_':
        move_count += 1
        moves.append(bottom_right_)

    if debug:
        print("move_count:")
        print(move_count)

    if not get_move:
        return move_count
    else:
        return moves


game_on = False
c_b = make_chessboard()
chessboard = c_b[0]
cell_width = c_b[1]


def start():
    global chessboard
    global game_on
    global cell_width

    try:
        move_ = set_position(chessboard, input_string="Enter the knight's starting position: ", cw=cell_width)
        chessboard = move_[0]
        game_on = True
    except TypeError:
        print("No moves possible!")
        start()


total_moves = 0


def set_position(cb, cw, input_string="Enter your next move: ", current_position=None):
    global game_on

    dimensions = get_dimensions(input_=input(input_string),
                                x_limit=((len(cb[1]) - (3 + (len(cb) - 3) // 10)) // (cw + 1)),
                                y_limit=len(cb) - 3)

    x___ = dimensions[0] * (cw + 1) + (2 - cw)
    y___ = len(cb) - dimensions[1] - 2

    while cb[y___][x___] in ['X', '0', ' ', '*'] and cb[y___][x___] != '_':
        print('invalid move', end='')
        dimensions = get_dimensions(input_=input(input_string),
                                    x_limit=((len(cb[1]) - (3 + (len(cb) - 3) // 10)) // (
                                            cw + 1)),
                                    y_limit=len(cb) - 3)
        x___ = dimensions[0] * (cw + 1) + (2 - cw)
        y___ = len(cb) - dimensions[1] - 2

    aux_board = []
    for row_ in cb:
        aux_board.append(row_)

    top_left = [x___ - 1 * (cw + 1) + cw - 1, y___ - 2]
    top_right = [x___ + 1 * (cw + 1) + cw - 1, y___ - 2]
    left_top = [x___ - 2 * (cw + 1) + cw - 1, y___ - 1]
    left_bottom = [x___ - 2 * (cw + 1) + cw - 1, y___ + 1]
    right_top = [x___ + 2 * (cw + 1) + cw - 1, y___ - 1]
    right_bottom = [x___ + 2 * (cw + 1) + cw - 1, y___ + 1]
    bottom_left = [x___ - 1 * (cw + 1) + cw - 1, y___ + 2]
    bottom_right = [x___ + 1 * (cw + 1) + cw - 1, y___ + 2]

    if current_position is not None:
        if get_possible_moves(x___ + 1, y___, cb, cw) == 0:
            game_on = False
        if cb[y___][x___] in ['X', ' ', '*']:
            print('invalid move', end='')
            return set_position(cb, cw, input_string, current_position)
        if current_position[0] not in [top_left[0] - 1, top_right[0] - 1, left_top[0] - 1, left_bottom[0] - 1,
                                       right_top[0] - 1, right_bottom[0] - 1, bottom_left[0] - 1, bottom_right[0] - 1] \
                or current_position[1] not in [top_left[1], top_right[1], left_top[1], left_bottom[1],
                                               right_top[1], right_bottom[1], bottom_left[1], bottom_right[1]]:
            print('invalid move', end='')
            return set_position(cb, cw, input_string, current_position)

    if cw == 3:
        x___ += 1

    temp = cb[y___]

    temp = temp[:x___] + (cw - 1) * ' ' + 'X' + temp[x___ + cw:]
    temp_aux = temp.replace('X', '*')

    del cb[y___]
    cb.insert(y___, temp)
    del aux_board[y___]
    aux_board.insert(y___, temp_aux)

    def rewrite_row(pos):
        if 3 < pos[0] < len(cb[0]) - 2 and 0 < pos[1] < len(cb) - 2 \
                and cb[pos[1]][pos[0]] not in ['X', '*']:
            tmp = cb[pos[1]][:pos[0] - (cw - 1)]
            tmp += (cw - 1) * ' ' + str(get_possible_moves(pos[0], pos[1], cb, cw))
            tmp += cb[pos[1]][pos[0] + 1:]
            del cb[pos[1]]
            cb.insert(pos[1], tmp)
            return cb

    rewrite_row(top_left)
    rewrite_row(top_right)
    rewrite_row(left_top)
    rewrite_row(right_top)
    rewrite_row(left_bottom)
    rewrite_row(right_bottom)
    rewrite_row(bottom_left)
    rewrite_row(bottom_right)

    for row_ in cb:
        print(row_)
    print()

    global total_moves
    total_moves += 1

    return [aux_board, x___, y___]


info = get_dimensions(input("Enter the knight's starting position: "), "Enter the knight's starting position: ",
                      x_limit=x, y_limit=y)
x_ = info[0] * (cell_width + 1) + (2 - cell_width)
y_ = len(chessboard) - info[1] - 2
cb_ = make_chessboard([x + 1, y])
total_moves += 1
cb_[0] = rewrite(x_ + (cell_width + 1), y_, cb_[0], cb_[1], total_moves)
total_moves += 1
sol = solution(x__=x_ + (cell_width + 1), y__=y_, cb=cb_[0], cw=cb_[1], tm=total_moves)

if get_game_mode():
    if len(solutions) > 0:
        print()
        print("Here's the solution!")
        n = 0
        for ch in solutions[:len(chessboard) - 1]:
            if n < len(chessboard) - 1:
                if cell_width == 3:
                    chessboard[n] = ch[:2] + ch[2 + (cell_width + 1) + 1:]
                else:
                    chessboard[n] = ch[:2] + ch[2 + (cell_width + 1):]
            n += 1
        chessboard[len(chessboard) - 1] = chessboard[len(chessboard) - 1][1:]
        ks = 0
        for cs in chessboard:
            if cs.count('_') > 0:
                cs = cs[:cs.find('_')] + (cell_width // 3) * ' ' + str((x - 1) * y) + cs[cs.find('_') + cell_width:]
                chessboard[ks] = cs
            ks += 1
        print_board(chessboard)
    else:
        print("No solution exists!")
else:
    if len(solutions) > 0:
        temp_board = []
        for chess in chessboard:
            temp_board.append(chess)
        chessboard = rewrite(x_, y_, chessboard, cell_width, '*')
        p_p = get_possible_moves(x_, y_, chessboard, cell_width, get_move=True)
        temp_board = rewrite(x_, y_, temp_board, cell_width, 'X')
        for p_ in p_p:
            temp_board = rewrite(p_[0], p_[1],
                                 temp_board, cell_width, get_possible_moves(p_[0], p_[1], chessboard, cell_width))
        print_board(temp_board)
        print()
        info = set_position(chessboard, cell_width, current_position=[x_, y_])
        x_ = info[1] * (cell_width + 1) + (2 - cell_width)
        y_ = len(chessboard) - info[2] - 2
        cb_ = make_chessboard([x + 1, y])
        if solution(x__=x_ + (cell_width + 1), y__=y_, cb=cb_, cw=cb_[1], tm=total_moves):
            game_on = True
            info = set_position(info[0], cell_width, current_position=[info[1], info[2]])
            board = info[0]
            while game_on:

                info = set_position(board, cell_width, current_position=[info[1], info[2]])
                board = info[0]

            else:
                game_completed = True
                for row in board:
                    if row.count("_") >= cell_width:
                        print("No more possible moves!")
                        print(f"Your knight visited {total_moves - 1} squares!")
                        game_completed = False
                        break
                if game_completed:
                    print("What a great tour! Congratulations!")
        else:
            print("No solution exists!")
    else:
        print("No solution exists!")
