def find_floor(line):
    floor = 0
    for element in line:
        if element == ('('):
            floor += 1
        if element == (')'):
            floor -= 1
    return floor


def find_pozition(line):
    characters = list(''.join(line))
    floor = 0
    for index in range(len(characters)):
        if characters[index] == ('('):
            floor += 1
        if characters[index] == (')'):
            floor -= 1
        if floor == -1:
            return (index+1)


def main():
    line = input()
    print(find_floor(line))


if __name__ == '__main__':
    main()
