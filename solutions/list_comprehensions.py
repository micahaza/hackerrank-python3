# https://www.hackerrank.com/challenges/list-comprehensions/problem


def list_compr():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ll = [[xa, ya, za] for xa in range(0, x + 1) for ya in range(0, y + 1) for za in range(0, z + 1) if xa + ya + za != n]
    print(ll)
