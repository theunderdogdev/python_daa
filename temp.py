import random


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def print_mat(matrix,rows, columns):
    if columns < 9:
        print(" ", *[i for i in range(0, columns)], sep="   ", end="  ")
    else:
        print(" ", *[i for i in range(0, 10)], sep="   ", end="  ")
    if columns > 10:
        print(*[i for i in range(10, columns)], sep="  ")
    else:
        print()
    for i, row in enumerate(matrix):
        if i <= 9:
            print(i, end="   ")
        else:
            print(i, end="  ")
        for col in row:
            print(col, end="  ")
        print()


colors = [colored(0, 255, 0, 'G'), colored(255, 0, 0, 'R'), colored(255, 255, 0, 'Y'), colored(153, 51, 255, 'P')]
mat = []
v = 'R'

for _ in range(20):
    temp = []
    for i in range(5):
        v = random.randint(0, len(colors) - 1)
        temp.append(colors[v])
    mat.append(temp)


for _ in range(3):
    print_mat(mat, 20,5)
