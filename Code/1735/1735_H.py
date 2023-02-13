import sys
sys.stdin = open('text.txt', 'r')

# a와 b의 최대공약수는 b와 a를 b로 나눈 나머지 의 최대공약수와 같다
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


a = list(map(int, input().split()))
b = list(map(int, input().split()))
x, y = a[0] * b[1] + a[1] * b[0], a[1] * b[1]
num = gcd(x, y)
print(x//num, y//num)