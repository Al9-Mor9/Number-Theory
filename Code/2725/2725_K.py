import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 유클리드 호제법
# 기울기 이용 - (1,2)와 (2,4)의 차이는 서로소냐 아니냐의 차이
# 최대공약수가 1이 되는 집합들을 찾아야 함

def gcd(i, j): # 최대공약수 구하는 함수
    while j != 0: # 유클리드 알고리즘
        i, j = j, i % j
    return i

shown = [0 for _ in range(1001)] # shown[n] -> n * n 정사각형 안에 조건을 만족하는 점의 수
shown[1] = 3 # (1,0)(1,1),(1,2)

for i in range(2, 1001):
    cnt = 0
    for j in range(1, i): # 왼쪽 아래 절반 삼각형
        if gcd(i, j) == 1: # 최대공약수가 1, 즉 (i, j)는 기울기가 다른 최초의 점
            cnt += 2 # 대칭
    shown[i] = shown[i-1] + cnt # 누적합

t = int(input())
for _ in range(t):
    n = int(input())
    print(shown[n])
                

# ---------------------------------------------------------------
# 에라토스테네스의 체(시간초과)
# r = 1001
# shown = [[True] * r for _ in range(r)]

# for i in range(2, r):
#     shown[i][0] = False # 첫 번째 열
#     shown[0][i] = False # 첫 번째 행
#     shown[i][i] = False # 대각선

# for i in range(2, r): # 왼쪽 아래 삼각형
#     for j in range(1, i):
#         d1 = i
#         d2 = j
#         if shown[i][j] == True:
#             while d1 + i < r and d2 + j < r:
#                 d1 += i
#                 d2 += j
#                 shown[d1][d2] = False 
#                 shown[d2][d1] = False # 에라토스테네스의 체

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     cnt = 0
#     for i in range(n + 1):
#         for j in range(n + 1):
#             if shown[i][j] == True:
                
#     print(cnt - 1)