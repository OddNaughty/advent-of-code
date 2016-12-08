import operator

def chunks(l, n):
    """
        Yield successive n-sized chunks from l.
        Imported from http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
    """
    for i in range(0, len(l), n):
        yield l[i:i + n]

def main():
    with open("inputs/03_input_real.txt") as f:
        instructions = [int(i) for l in f.readlines() for i in l.strip().split()]
        in_columns = [triangle for i in range(3) for triangle in list(chunks(instructions[i::3], 3))]
        filtered = [e for e in in_columns if e[0] + e[1] > e[2] and e[0] + e[2] > e[1] and e[1] + e[2] > e[0]]
        print(len(filtered))

# Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.
#
# For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:
#
# 101 301 501
# 102 302 502
# 103 303 503
# 201 401 601
# 202 402 602
# 203 403 603
# In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?
#
# Although it hasn't changed, you can still get your puzzle input.



if __name__ == '__main__':
    main()
