def main():
    with open("04_input.txt") as f:
        rooms = [l.strip() for l in f.readlines()]
        for room in rooms:
            splitted = line.split('-')
            name, checksum = "".join(splitted[:-1])

if __name__ == '__main__':
    main()
