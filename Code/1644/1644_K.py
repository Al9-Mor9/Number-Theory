import sys
sys.stdin = open('input.txt.', 'r')

n = int(input())
ans = 0
primes = []
arr = [0, 0] + [1] * (n-1)

# 에라토스테네스의 체로 n이하의 소수 저장(primes)
for i in range(2, n+1):
    if arr[i] == 1:
        primes.append(i)
        for j in range(2*i, n+1, i):
            arr[j] = 0

# 투 포인터
end = 0
interval_sum = 0 # start와 end 사이의 구간 합
for start in range(len(primes)):
    while interval_sum < n and end < len(primes): # 구간합이 n보다 크거나 같아질 때까지
        interval_sum += primes[end] # n보다 작으면 다음 숫자를 더해감
        end += 1
    if interval_sum == n: # 구간합이 n과 같아졌을 때
        ans += 1
    interval_sum -= primes[start] # 첫 숫자를 빼고 다시 진행
print(ans)



# ----------------------------------------------------------------------
# 시간 초과 될 것 같은 코드...(에라토스테네스의 체 + 누적합 간의 차 사용)
# 소수 배열을 소수의 누적합 배열로 바꿈
# for i in range(1, len(primes)):
#     primes[i] += primes[i-1]

# n이 소수일 경우 경우의 수 +1
# if primes[-1] - primes[-2] == n:
#     ans += 1

# for i, p in enumerate(primes):
#     if p == n:          # 소수의 누적합 중 n이 있으면 경우의 수 +1
#         ans += 1
#     elif p > n:         # 소수의 누적합이 n보다 커진 직후 index 저장
#         start = i
#         break

# flag = 1
# if start == len(primes) - 1:
#     flag = 0

# idx = 0

# while flag:
#     for i in range(idx, start-1):
#         s = primes[start] - primes[i]
#         if s == n:
#             ans += 1
#         elif s < n:
#             idx = i
#             start += 1
#         elif i == start - 2 and s > n:
#             flag = 0
#             break
# print(ans)