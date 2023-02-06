import sys
sys.stdin = open("input_2725.txt", "r")
#------------#
import sys
def gcd(a, b):  # i, j 즉, a, b가 서로소(최대공약수가 1)이면 리턴 트루
    while b > 0:    # 그래서 여기서 a, b 유클리드 알고리즘 적용
        a, b = b, a % b
    if a == 1:  # 최대공약수가 1이면 서로소임
        return True
    else:
        return False

arr = [[0] for _ in range(1001)]    # 선분 수를 담을 list 초기화
arr[1] = 1
for i in range(2, 1001):    # 서로소의 갯수 누적하는 반복문
    cnt = 0
    for j in range(1, i):   # i j = 2 1, 3 1, 3 2, 4 1, 4 2, 4 3, ..., 1000 998, 1000 999
        if gcd(i, j):   # i, j 서로소 확인
            cnt += 1    # i번째 줄이 추가되면 추가되는 선분 수만큼 더함(반쪽짜리)
    arr[i] = arr[i-1] + cnt

T = int(sys.stdin.readline())
for tc in range(T):
    n = int(sys.stdin.readline())
    print(1 + 2 * arr[n]) # 반대쪽 + 가운데 딱 하나