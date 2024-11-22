import re


def find_floor():
    file = open(r"C:\Users\dande\Desktop\input.txt", "r")
    lines = file.readlines()
    file.close()
    sum = 0
    for line in lines:
        for element in line:
            if element == ('('):
                sum += 1
            if element == (')'):
                sum -= 1
        print(sum)


def main():
    print(find_floor(input()))


if __name__ == '__main__':
    main()
