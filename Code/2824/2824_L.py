import sys
sys.stdin = open("input_2824.txt", "r")

import sys

n = int(sys.stdin.readline())
arr_n = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr_m = list(map(int, sys.stdin.readline().split()))

a, b = 1, 1     
for i in arr_n:
    a *= i
for j in arr_m:
    b *= j

def Ec(a, b):
    while b!= 0:
        r = a % b
        a = b
        b = r
    return a

gcd = str(Ec(a, b))
gcd = gcd[-9:] if len(gcd) > 9 else gcd
print(gcd)
