import sys
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

forward_gcd = [0] * n
backward_gcd = [0] * n 

forward_gcd[0] = arr[0]
backward_gcd[-1] = arr[-1]

for i in range(1, n - 1):
    forward_gcd[i] = gcd(forward_gcd[i - 1], arr[i])

for i in range(n - 2, 0, -1):
    backward_gcd[i] = gcd(arr[i], backward_gcd[i + 1])

idx = 0 
max_ = backward_gcd[1]
for i in range(1, n - 2):
    tmp = gcd(forward_gcd[i - 1], backward_gcd[i + 1])
    if tmp > max_:
        max_ = tmp
        idx = i

if max_ < forward_gcd[-2]:
    max_ = forward_gcd[-2]
    idx = n

if arr[idx] % max_ == 0:
    print(-1)
else:
    print(max_, arr[idx])
