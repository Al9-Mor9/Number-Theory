import sys
sys.stdin = open("input.txt", "r", encoding="UTF-8")
#-------------------------------------------------------------
import sys

sys.stdin.readline()
arr = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
def gcd(a, b):
    while b: a, b = b, a % b
    return a
# [kx + 1 = cy] 를 만족하는 y를 구해야 한다. 
for kc in arr:
    k, c = kc[0], kc[1]
    # 만약 서로소가 아니면, 해가 없다. 
    if gcd(k, c) != 1 or k + 1 > 1e9: print("IMPOSSIBLE")
    # 사탕 봉지당 사탕이 하나 들어있다면, 
    # kx + 1개를 사면된다. 돈을 아껴서 인당 k + 1개만 주자.
    elif c == 1: print(k + 1)
    # 친구가 한명이면, 사탕봉지 하나만 사서 다 주면 된다.....
    elif k == 1: print(1)
    else:
        a, b = k, c
        s, s_ = 1, 0
        t, t_ = 0, 1
        while b:
            # 얼마나 필요한지 누적해서 더해주는 꼴이다.
            # t가 음수인 경우를 보자.
            print(f"a: {a}, b: {b}, r: {a%b}")
            print(f"s: {s}, t: {t}")
            print(f"s_: {s_}, t_: {t_}")
            
            q, a, b = a // b, b, a % b
            s__ = s - q * s_
            t__ = t - q * t_
            print(f"s__: {s__}, t__: {t__}\n=========")
            
            s, s_ = s_, s__
            t, t_ = t_, t__
        #t가 음수라면, 양수가 될 때까지, k를 더해주자. 
        # kx + 1 = cy 에서
        # ks + 1 = ct 로 생각하면
        # ks + 1 + nkc = ct + nkc
        # k(s + nc) + 1 = c(t + nk)
        # kx + 1 = c(t + nk)
        # 위와 같이 음수해를 양수해로 바꿀 수 있다.
        if t < 0: t = (t % k + k) % k
        print(t, "\n\n")
