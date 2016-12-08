from collections import Counter
from operator import itemgetter


def main():
    with open("inputs/06_input_real.txt") as f:
        decoded = ''
        messages = [m.strip() for m in f.readlines()]
        rotated = list(zip(*messages))
        for col in rotated:
            counter = Counter(col)
            decoded += min(counter.items(), key=itemgetter(1))[0]
        print(decoded)

if __name__ == '__main__':
    main()
