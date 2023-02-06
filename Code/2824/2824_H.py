import sys
sys.stdin = open('input_2824.txt', 'r')
# ------------
import sys
# from math import gcd

def gcd(a, b):  # 유클리드 호제법
    if b > a:   # 항상 a가 크도록
        a, b = b, a
    # a를 b로 나눈 나머지와 b의 최대 공약수는 a와 b의 최대 공약수와 같다
    # 그럼, 계속해서 a를 b로 나누어서 b를 a에 나눈 나머지를 b에 대입시켜 b가 0이 될때까지 반복하면
    # 남는 a 값이 최대 공약수
    while b > 0:
        a, b = b, a % b
    return a


n = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))
a, b = 1, 1
for i in N:
    a *= i
for i in M:
    b *= i

print(str(gcd(a, b))[-9:])
