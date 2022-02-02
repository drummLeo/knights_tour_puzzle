def get_dimensions(input_, x_limit=99, y_limit=99):
    try:
        input_list = input_.split()
        dimension = [int(input_list[0]), int(input_list[1])]
    except IndexError:
        print("Invalid dimensions!")
        return get_dimensions(input_=input("> "), x_limit=x_limit, y_limit=y_limit)
    except ValueError:
        print("Invalid dimensions!")
        return get_dimensions(input_=input("> "), x_limit=x_limit, y_limit=y_limit)
    else:
        if dimension[0] < 1 or dimension[1] < 1:
            print("Invalid dimensions!")
            return get_dimensions(input_=input("> "), x_limit=x_limit, y_limit=y_limit)
        if dimension[0] > x_limit or dimension[1] > y_limit:
            print("Invalid dimensions!")
            return get_dimensions(input_=input("> "), x_limit=x_limit, y_limit=y_limit)

        return [dimension[0], dimension[1]]


def make_chessboard():
    dimensions = get_dimensions(input_=input("Type the board dimensions:\n> "))
    x = dimensions[0]
    y = dimensions[1]

    cell_width_ = 1
    if x * y >= 9:
        cell_width_ = 2
    if x * y >= 81:
        cell_width_ = 3

    chessboard = []

    for i in range(1, y + 1):
        row_ = f" {i}|" + (x * f" {cell_width_ * '_'}") + ' |'
        if y + 1 >= 10:
            row_ = ' ' + row_
        chessboard.append(row_)

    border = ' ' + (3 + (cell_width_ + 1) * x) * '-'
    chessboard.insert(0, border)
    chessboard.append(border)

    chessboard = chessboard[::-1]

    return [chessboard, cell_width_]


aux = make_chessboard()
board = aux[0]
cell_width = aux[1]


def set_position(chessboard):
    dimensions = get_dimensions(input_=input("Type the horse next position:\n> "),
                                x_limit=((len(chessboard[1]) - (3 + (len(chessboard) - 2) // 10)) // (cell_width + 1)),
                                y_limit=len(chessboard) - 2)

    x = dimensions[0] * (cell_width + 1) + (2 - cell_width)
    y = len(chessboard) - dimensions[1] - 1

    if cell_width == 3:
        x += 1

    temp = chessboard[y]

    temp = temp[:x] + (cell_width - 1) * ' ' + 'X' + \
        temp[x + cell_width:]

    del chessboard[y]
    chessboard.insert(y, temp)

    return chessboard


set_position(board)

for row in board:
    print(row)
