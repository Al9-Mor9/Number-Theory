import sys
sys.stdin = open("input.txt", "r")

# 그림을 보면, 대각을 기준으로 대칭이다, 아래 부분의 직선 수를 n 이라고하면, 총 선분 수는 2n + 1 
# n의 범위가 1000이므로, 각 선분 수를 누적하면서 저장하자.
# n - 1에서 n이 될 때, n에 대한 서로소의 개수를 검사하면 된다.
import sys
def euler_phi(n):
    cnt = n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            cnt -= cnt / i
    if n > 1:                           # 만약 n이 소수라면 모든 수와 서로소이다. euler_phi : n-1
        cnt -= cnt / n
    return int(cnt)

arr = [0] * 1001
arr[1] = 1                              #1은 제외, 그림에선 기울기가 0인 놈
for i in range(2, 1001):
    arr[i] = arr[i-1] + euler_phi(i)    #서로소의 개수를 누적하자.

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(1 + 2*arr[n])                 # 가운데와 반대쪽을 고려해주자.
