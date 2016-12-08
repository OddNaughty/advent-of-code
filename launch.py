import os
import re

def main():
    pattern_exec_files = re.compile(r"^[0-9]+\.py$")
    for f in sorted(filter(pattern_exec_files.match, os.listdir())):
        print("Executing {} !".format(f))
        os.system("python3 {}".format(f))
        print()

if __name__ == '__main__':
    main()
