# PyPy3로 정답
import sys
# sys.stdin = open('input.txt', 'r')
array = [True] * 1000001 # 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
# 에라토스테네스의 체 알고리즘
for i in range(2, 1000001):  # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i]:  # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수 = False
        j = 2
        while i * j <= 1000000:
            array[i * j] = False
            j += 1

n = int(sys.stdin.readline())
while n != 0:
    ans = True
    for i in range(3, n):
        if array[i] and array[n-i]: # i와 n-i가 소수일 때 출력
            print(f'{n} = {i} + {n-i}')
            ans = False # 플래그 False
            break
    if ans: # 플래그 True로 있으면
        print("Goldbach's conjecture is wrong.")
        n = int(sys.stdin.readline())   # 출력하고 다음줄
        continue
    n = int(sys.stdin.readline())