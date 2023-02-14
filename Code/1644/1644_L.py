import sys
sys.stdin = open("input.txt", "r", encoding="UTF-8")
#-------------------------------------------------------------
import sys

n = int(sys.stdin.readline())
if n == 0 or n == 1:
    print(0)
    sys.exit()

arr = [True] * (n + 1)
arr[0] = False
arr[1] = False

for i in range(2, int(n ** 0.5) + 1):
    j = 2
    while i * j < n + 1:
        arr[i * j] = False
        j += 1

arr = [i for i in range(n+1) if arr[i]]
p1, p2, tmp, ans = 0, 1, arr[0], 0

while p2 < len(arr) + 1:
    if tmp == n: 
        ans += 1
        if p2 ==len(arr):break
        tmp += arr[p2]
        p2 += 1
    elif tmp < n:
        if p2 ==len(arr):break
        tmp += arr[p2]
        p2 += 1        
    else:
        tmp -= arr[p1]
        p1 += 1
print(ans)