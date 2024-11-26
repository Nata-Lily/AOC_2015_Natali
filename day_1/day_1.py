def find_floor(line):
    floor = 0
    for element in line:
        if element == ('('):
            floor += 1
        if element == (')'):
            floor -= 1
    return floor


def main():
    line = input()
    print(find_floor(line))


if __name__ == '__main__':
    main()
