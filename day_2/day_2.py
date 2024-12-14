#! /usr/bin/env python

import functools
import re


def find_square_wrapping_paper(file):
   # file = open(r"C:\Users\dande\Desktop\input_day_2.txt", "r")
    lines = file.splitlines()
    new = []
    for line in lines:
        new.append(line.split('x'))
    c = []
    for i in range(len(new)):
        for el in new[i]:
            c.append(int(el))
    res = [c[i:i+3] for i in range(0, len(c), 3)]
    result = []
    for i in range(len(res)):
        a = res[i]
        for k in range(len(a)):
            for j in range(k + 1, len(a)):
                result.append(a[k]*a[j])
    min_wrapping_paper = [result[i:i+3] for i in range(0, len(result), 3)]
    min_wrapping_paper_result = []
    for i in range(len(min_wrapping_paper)):
        min_wrapping_paper_result.append(min(min_wrapping_paper[i]))

    return sum(result) * 2 + sum(min_wrapping_paper_result)


def main():
    file = input()
    print('We need', find_square_wrapping_paper(file),'feets of wrapping paper')


if __name__ == '__main__':
    main()
