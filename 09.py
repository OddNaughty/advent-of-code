import re


def count_da_shit(s):
    i, tot = 0, 0
    while i < len(s):
        if s[i] != "(":
            tot += 1
            i += 1
        else:
            i += 1
            i2 = i
            while s[i2] != ")":
                i2 += 1
            capturing = s[i:i2]
            i = i2 + 1
            nb_char, times = [int(c) for c in capturing.split("x")]
            to_copy = s[i:i + nb_char]
            i += nb_char
            tot += count_da_shit(to_copy) * times
    return tot


def main():
    with open("inputs/09_input_real.txt") as f:
        instructions = [re.sub("\s", "", l) for l in f]
        for instruction in instructions:
            tot = count_da_shit(instruction)
            print(tot)

if __name__ == '__main__':
    main()
