from random import randint


def create_grid(rows, cols, value):
    grid = [[value for _ in range(cols)] for _ in range(rows)]
    return grid


def get_neighbors(rows, cols, r, c):
    list_coord = []
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if r+i >= 0 and r+i < rows:
                if c+j >= 0 and c+j < cols:
                    if not (i == 0 and j == 0):
                        list_coord.append([r+i, c+j]) 

    return list_coord


def print_grid(grid):
    for i in grid:
        for j in i:
            print(j, end="")
        print('')


def generate_mines(rows, cols, nb_mines, forbidden_cell):
    mines = []
    arround_forbidden_cell = get_neighbors(rows, cols, forbidden_cell[0], forbidden_cell[1])
    for i in range(nb_mines):
        place = True
        while place:
            x = randint(0, rows-1)
            y = randint(0, cols-1)
            if not ((x, y) in mines or (x, y) == forbidden_cell or [x, y] in arround_forbidden_cell):
                mines.append((x, y))
                place = False
    return mines


def create_hidden_grid(rows, cols, mines):
    internal_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for (i, j) in mines:
        internal_grid[i][j] = '*'
        neighbors = get_neighbors(rows, cols, i, j)
        for k, l in neighbors:
            if (k, l) not in mines:
                internal_grid[k][l] += 1

    return internal_grid


def reveal(hidden, visible, r, c):

    if hidden[r][c] == 0 and visible[r][c] == '#':
        visible[r][c] = hidden[r][c]
        neighbors = get_neighbors(len(hidden), len(hidden[0]), r, c)
        for i, j in neighbors:
            reveal(hidden, visible, i, j)
    
    elif hidden[r][c] != 0 and visible[r][c] != 'F':
        visible[r][c] = hidden[r][c]


def has_won(visible, nb_mines):
    c_2 = [el for row in visible for el in row].count('#')
    c_2 += [el for row in visible for el in row].count('F')
    return nb_mines == c_2


def has_lost(visible):
    c = [el for row in visible for el in row].count('*')
    if c != 0:
        return True
    else:
        return False
    

def validation(command, rows, cols):
    coord_valid = True
    r, c = -1, -1
    if len(command) == 3:
        if command[1].isdigit():
            r = int(command[1])
            if command[2].isdigit():
                c = int(command[2])
                if r >= 0 and r < rows and c >= 0 and c < cols:
                    coord_valid = False

    return coord_valid


def minesweeper(rows, cols, nb_mines):
    visible = create_grid(rows, cols, '#')
    print_grid(visible)
    coord_valid = True
    generate = False
    mines = []
    hidden = [[]]
    
    end = True
    while end:
        
        coord_valid = True
        while coord_valid:
            command = input('Command (o row col/ f row col): ').split(' ')
            coord_valid = validation(command, rows, cols)
            
        r = int(command[1])
        c = int(command[2])

        if not generate:
            mines = generate_mines(rows, cols, nb_mines, (r, c))
            hidden = create_hidden_grid(rows, cols, mines)
            generate = True

        if command[0] == 'o':
            if visible[r][c] == '#':
                reveal(hidden, visible, r, c)
        if command[0] == 'f':
            if visible[r][c] == '#':
                visible[r][c] = 'F'
            elif visible[r][c] == 'F':
                visible[r][c] = '#'
            else:
                print('Vous ne pouvez flaguer une case révélée')
        
        print_grid(visible)

        if has_lost(visible):
            print('You loose')
            end = False

        if has_won(visible, nb_mines):
            
            print('You win')
            end = False


minesweeper(10, 20, 80)


