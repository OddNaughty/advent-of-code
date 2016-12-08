import operator


def limit_to(grid, old_one, to_move):
    new_y, new_x = old_one[0] + to_move[0], old_one[1] + to_move[1]
    try:
        assert grid[new_y][new_x] != 0 and new_y >= 0 and new_x >= 0
    except Exception:
        return old_one
    return (new_y, new_x)


def main():
    with open("02_input_real.txt") as f:
        nb_map = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, 'A', 'B', 'C', 0], [0, 0, 'D', 0, 0]]
        test = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        where_am_i = (2, 0)
        instructions = [list(l.strip()) for l in f.readlines()]
        for line in instructions:
            for direction in line:
                where_am_i = limit_to(nb_map, where_am_i, test[direction])
            print(nb_map[where_am_i[0]][where_am_i[1]], end='')

if __name__ == '__main__':
    main()
