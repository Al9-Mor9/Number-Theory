import sys
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
max_ = max(arr)

# 1000000이하의 소수 구하기.
prime_n = 1000000
prime_lst = [True] * prime_n
for i in range(2, int(prime_n ** 0.5) + 1):
    j = 2
    while i * j < prime_n:
        if prime_lst[i * j]:
            prime_lst[i * j] = False
        j += 1

prime_lst = [i for i in range(2, prime_n) if prime_lst[i]]
lst = [0] * len(prime_lst)

def fact(k):
    idx = 0
    while k >= prime_lst[idx]:
        if not k % prime_lst[idx]:
            k //= prime_lst[idx]
            lst[idx] += 1
        else:
            idx +=1
    
for i in arr:
    fact(i)
for i in range(len(prime_lst)):
    if prime_lst[i] >= max_:
        max_ = i
        break

lst = lst[:max_]
prime_lst = prime_lst[:max_]

print(lst)
print(prime_lst)
print(n)
gcd = 1
for i in range(len(lst)):
    if lst[i] and lst[i] % n == 0:
        print(i, lst[i], prime_lst[i], lst[i]//n)
        gcd *= prime_lst[i] ** (lst[i]//n)
print(gcd)