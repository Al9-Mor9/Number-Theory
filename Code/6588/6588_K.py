import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

r= 1000000
prime = [True for _ in range(r)]
for i in range(2, int(r**0.6)):
    if prime[i] == True:
        for j in range(i * 2, r, i) : 
            if prime[j] == True :
                prime[j] = False            #에라토스테네스의 체

while True:
    n = int(input())
    if n == 0: 
        break
    for i in range(3, r):
        if prime[i] == True and prime[n - i] == True:
                print(f"{n} = {i} + {n - i}")
                break
        

# 시간초과
# while True:
#     n = int(input())
#     if n == 0: # 입력이 0이면 멈춤
#         break
#     else:
#         plist = [0, 0] + [1] * (n - 1) # index가 0, 1인(소수가 아닌) 배열은 0, 2 이상부터 1로 맞춤(0 ~ n) 
#         for i in range(2, int((n + 1) ** 0.5) + 1): # 2부터 시작
#             if plist[i] != 0: # 지워지지 않은 숫자(에라토스테네스의 체)
#                 for j in range(2 * i, n + 1, i): # i의 2배부터 시작해서 n까지 배수를 모두 지움
#                     plist[j] = 0
    
#     flag = 0
#     for i in range(3, n + 1): # 소수 순회
#         if plist[i] and plist[n - i]:# 더해서 n이 되는 숫자도 소수인 경우(처음이기 때문에 차가 가장 큼)
#             print(f'{n} = {i} + {n-i}')
#             flag = 1
#             break
    
#     if flag == 0:
#         print("Goldbach's conjecture is wrong.")