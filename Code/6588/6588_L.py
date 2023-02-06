import sys
sys.stdin = open("input_6588.txt", "r")
from sys import stdin

arr = [True for i in range(1000001)]
for i in range(2, int(1000001 ** 0.5) + 1):
    if arr[i]:
        j = 2
        while i * j < 1000001:
            arr[i*j] =False
            j += 1

while True:
    n = int(stdin.readline())
    if n == 0: break
    for i in range(3, len(arr)):
        if arr[i] and arr[n-i] :
            print(f"{n} = {i} + {n-i}")
            break

