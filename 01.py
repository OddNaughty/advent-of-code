import operator


def choose_orientation(ori, prev):
    L = 'kaka'


def main():
    with open("inputs/01_input_real.txt") as f:
        test = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ori = 0
        visited = [(0, 0)]
        start = (0, 0)
        instructions = f.readline().strip().split(", ")
        for instruction in instructions:
            direction, n = instruction[0], int(instruction[1:])
            ori = (ori - 1 if direction == "L" else ori + 1) % 4
            # orientation[direction] = (orientation[direction] + 1) % 4
            to_add = (x * n for x in test[ori])
            old_y, old_x = start
            start = tuple(map(operator.add, start, to_add))
            y, x = start
            for i in range(old_x + 1, x + 1):
                if (y, i) in visited:
                    print(abs(y) + abs(i))
                    return
                visited.append((y, i))
            for i in range(old_y + 1, y):
                if (i, x) in visited:
                    print(abs(i) + abs(x))
                    return
                visited.append((i, x))

if __name__ == '__main__':
    main()
