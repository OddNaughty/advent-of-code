X_SIZE = 50
Y_SIZE = 6


def do_rect(grid, args):
    need_x, need_y = [int(i) for i in args[0].split('x')]
    for x in range(need_x):
        for y in range(need_y):
            grid[y][x] = '#'


def do_rotate(grid, args):
    affect, which, _, times = args
    which = int(which.split('=')[1])
    times = int(times)
    if affect == "column":
        # new_grid = ['#' i else '-' for i in range(X_SIZE * Y_SIZE)]
        new_grid = [[grid[y][x] if x != which else '-' for x in range(X_SIZE)] for y in range(Y_SIZE)]
        for y in range(Y_SIZE):
            if grid[y][which] == '#':
                new_y = (y + times) % Y_SIZE
                new_grid[new_y][which] = "#"
    else:
        new_grid = [[grid[y][x] if y != which else '-' for x in range(X_SIZE)] for y in range(Y_SIZE)]
        for x in range(X_SIZE):
            if grid[which][x] == '#':
                new_x = (x + times) % X_SIZE
                new_grid[which][new_x] = "#"
    return new_grid


def pretty_print(grid):
    for y in range(Y_SIZE):
        for x in range(X_SIZE):
            print(grid[y][x], end=' ')
        print()


def main():
    grid = [['-' for _ in range(X_SIZE)] for _ in range(Y_SIZE)]
    with open("inputs/08_input_real.txt") as f:
        instructions = [l.strip().split() for l in f]
        for instruction in instructions:
            cmd, args = instruction[0], instruction[1:]
            if cmd == "rect":
                do_rect(grid, args)
            else:
                grid = do_rotate(grid, args)
            pretty_print(grid)
            print('_______________________________________')
        lit = 0
        for x in range(X_SIZE):
            for y in range(Y_SIZE):
                if grid[y][x] == "#":
                    lit += 1
        print(lit)


if __name__ == '__main__':
    main()
