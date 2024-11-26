def find_floor(lines):
    #file = open(r"input.txt", "r")
    #lines = file.readlines()
    #file.close()
    lines = input()
    floor = 0
    for line in lines:
        for element in line:
            if element == ('('):
                floor += 1
            if element == (')'):
                floor -= 1
    return floor


def main():
    lines = input()
    print(find_floor(lines))


if __name__ == '__main__':
    main()
