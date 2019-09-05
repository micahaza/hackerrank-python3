# https://www.hackerrank.com/challenges/write-a-function/problem


def is_leap():
    year = int(input())
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0 and year % 400 != 0:
            leap = False
    print(leap)
