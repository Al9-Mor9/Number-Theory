import sys
sys.stdin = open('init.txt', 'r')
# 최대공약수가 1을 만족하는 자연수 1 < k < n의 갯수
# 오일러 피 함수 사용
#####
n = int(input())
ans = n

for i in range(2, round(n ** 0.5) + 1):
    # i가 n의 약수이면
    if n % i == 0:

        while n % i == 0:
            # 소수가 될 때까지 나눔
            n //= i
        # ans에다가 오일러 곱 공식 적용
        ans *= ((i - 1) / i)
# n이 1보다 크면 == 소수이면
if n > 1:
    # ans에다가 오일러 곱 공식 '한번'적용 (해도 괜찮!)
    ans *= ((n - 1) / n)
print(round(ans))
