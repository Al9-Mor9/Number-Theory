import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
mula = 1
mulb = 1
for num in a:
    mula *= num
for num in b:
    mulb *= num

if mula < mulb:
    mula, mulb = mulb, mula # A가 B보다 항상 크도록

while mulb != 0: # 유클리드 알고리즘
    r = mula % mulb
    mula = mulb
    mulb = r

print(str(mula)[-9:])