# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


def find_second_max():
    n = int(input()) # noqa
    arr = map(int, input().split())
    new_arr = sorted(list(set(arr)))
    if len(new_arr) == 1:
        print(new_arr[0])
    else:
        print(new_arr[len(new_arr) - 2])
