import hashlib

def main():
    start_pass = "ugkcyxxp"
    start_index = 0
    out = ['' for i in range(8)]
    numbers = [str(i) for i in range(10)]
    for i in range(8):
        digested = hashlib.md5((start_pass + str(start_index)).encode()).hexdigest()
        while not (digested.startswith('00000') and digested[5] in numbers and int(digested[5]) < 8 and out[int(digested[5])] == ''):
            digested = hashlib.md5((start_pass + str(start_index)).encode()).hexdigest()
            start_index += 1
        out[int(digested[5])] = digested[6]
        print(out)
        start_index += 1

if __name__ == '__main__':
    main()
