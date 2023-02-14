import sys
sys.stdin = open("input.txt", "r", encoding="UTF-8")
#-------------------------------------------------------------
import sys
import math

def check(a):
    num = 0.0
    for i in range(n):
        tmp = (a-arr[i][0])**2 + arr[i][1]**2
        if num < tmp: num = tmp
    return num

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    arr = [list(map(float, sys.stdin.readline().strip().split())) for _ in range(n)]
    sys.stdin.readline()
    
    l = -200000
    r = 200000
    ans = 0.0
    
    while r-l > 1e-9:
        thrid_1 = l + ((r - l) / 3)
        thrid_2 = l + ((r - l)*2 / 3)
        print("l: %.9f, thrid_1: %.9f, thrid_2: %.9f, r: %.9f" %(l, thrid_1, thrid_2, r))
        if check(thrid_1) > check(thrid_2):
            ans = thrid_1
            l = thrid_1
        else:
            ans = thrid_2
            r = thrid_2
    print("%.9f %.9f" % (ans, math.sqrt(check(ans))))