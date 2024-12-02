#! /usr/bin/env python
def find_floor(line):
    floor = 0
    for instruction in line:
        if instruction == '(':
            floor += 1
        if instruction == ')':
            floor -= 1
    return floor


def first_descent_into_the_basement(line):
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
    print('The floor Santa ends up on', find_floor(line))
    print(
        'When Santa descends into the basement',
        first_descent_into_the_basement(line)
    )


if __name__ == '__main__':
    main()
