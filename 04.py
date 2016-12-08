from collections import Counter
from operator import itemgetter
from string import ascii_lowercase
import re


def caesar_sipher(character, shift):
    if character in ascii_lowercase:
        return ascii_lowercase[(ascii_lowercase.index(character) + shift) % len(ascii_lowercase)]
    elif character == '-':
        return ' '
    return character


def main2():
    with open("inputs/04_input_real.txt") as f:
        rooms = [l.strip() for l in f.readlines()]
        for room in rooms:
            splitted = room.split('-')
            room_id, checksum = re.match(r"([0-9]+)\[(.+)\]", splitted[-1]).groups()
            new_name = "".join(list(map(lambda l: caesar_sipher(l, int(room_id)), "-".join(splitted[:-1]))))
            if "north" in new_name:
                print(new_name, room_id, checksum)


def main():
    sum_id = 0
    with open("inputs/04_input_real.txt") as f:
        rooms = [l.strip() for l in f.readlines()]
        for room in rooms:
            splitted = room.split('-')
            counter = Counter("".join(splitted[:-1]))
            to_checksum = sorted(dict(counter).items(), key=itemgetter(1), reverse=True)
            checksum_dict = {}
            for i in to_checksum:
                if i[1] not in checksum_dict:
                    checksum_dict[i[1]] = []
                checksum_dict[i[1]].append(i[0])
            meh = ""
            for a in sorted(checksum_dict, reverse=True):
                meh += "".join(sorted(checksum_dict[a]))
            room_id, checksum = re.match(r"([0-9]+)\[(.+)\]", splitted[-1]).groups()
            if checksum == meh[:5]:
                sum_id += int(room_id)
            print(meh[:5], room_id, checksum)
    print(sum_id)

if __name__ == '__main__':
    main2()
