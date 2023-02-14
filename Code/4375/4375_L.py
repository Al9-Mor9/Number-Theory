import sys
sys.stdin = open("input.txt", "r", encoding="UTF-8")


def gcd(a, b):
    while b: a, b = b, a % b
    return a
arr = list(map(int, sys.stdin.readlines()))
for i in arr:
    g = 1
    while gcd(i, g) % i:
        g = g * 10 + 1
    print(len(str(g)))