def find_floor(line):
    floor = 0
    for element in line:
        if element == '(':
            floor += 1
        if element == ')':
            floor -= 1
    return floor


def first_down_basement(line):
    floor = 0
    for index in range(len(line)):
        if line[index] == '(':
            floor += 1
        if line[index] == ')':
            floor -= 1
        if floor == -1:
            return index + 1


def main():
    line = input()
    print(
        find_floor(line),
        f'first_down_basement = {first_down_basement(line)}'
    )


if __name__ == '__main__':
    main()
