import re


def chunks_by(l, chunk_size, step=1):
    for i in range(0, len(l), step):
        yield l[i:i + chunk_size]


def abba(l):
    valid_ones = []
    for el in l:
        for chunk in chunks_by(el, 3):
            if len(chunk) > 2 and chunk[0] == chunk[2]:
                valid_ones.append(chunk)
    return valid_ones


def main():
    with open("inputs/07_input_real.txt") as f:
        ips = [ip.strip() for ip in f.readlines()]
        abbas = []
        for ip in ips:
            sequences = re.split(r"\[|\]", ip)
            need_abba = list(filter(None, abba(sequences[::2])))
            no_need_abba = list(filter(None, abba(sequences[1::2])))
            for i in need_abba:
                if ip in abbas:
                    break
                for j in no_need_abba:
                    if i[1] == j[0] and i[0] == j[1]:
                        abbas.append(ip)
                        break
        print(len(abbas))


if __name__ == '__main__':
    main()
