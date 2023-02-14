import sys
sys.stdin = open("input.txt", "r", encoding="UTF-8")
#-------------------------------------------------------------
import sys

nlst = list(map(lambda x : int(x.strip()), sys.stdin.readlines()))
print(nlst)
for n in nlst:
    print("\n----------------")
    if n == 0 or n == 1:
        print(0)
        sys.exit()

    # 0 부터 n까지 n + 1 개
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    # 에라토스뭐시기
    for i in range(2, int(n ** 0.5) + 1):
        j = 2
        while i * j < n + 1:
            arr[i * j] = False
            j += 1

    print(f"n: {n} \narr: \n{arr}\n")
    
    # n이하의 소수 집합
    arr = [i for i in range(n + 1) if arr[i]]
    arr.append(0)
    print(f"-----> {arr}")
    p1, p2, tmp, ans = 0, 1, arr[0], 0

    # 투 포인터로 찾아보자!
    while p2 < len(arr):
        if tmp == n:
            print(f"\n    p1, p2 = {p1}, {p2}") 
            print(f"    arr = ",arr[p1 : p2])
            ans += 1
            tmp += arr[p2]
            tmp -= arr[p1]
            p2 += 1
            p1 += 1
        elif tmp < n:
            tmp += arr[p2]
            p2 += 1
        else:
            tmp -= arr[p1]
            p1 += 1            
    print(ans)
