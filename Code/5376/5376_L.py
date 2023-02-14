import sys
sys.stdin = open("input.txt", "r", encoding="UTF-8")
#-------------------------------------------------------------
import sys

def d_gcd(a, b):
    x, y = a, b
    while b: a, b = b, a % b
    x //= a
    y //= a
    return x, y

sys.stdin.readline()
arr = list(map(lambda x: x.rstrip(")\n").replace("0.",""), sys.stdin.readlines()))
for rd in arr:
    if "(" not in rd:
        x, y = d_gcd(int(rd), int('1' + '0' * len(rd)))
    else:
        a, b = rd.split("(")
        if a == '':
            x, y = d_gcd(int(b), int('1' + '0' * len(b)) - 1)
        else:
            x, y = d_gcd((int(a + b) - int(a)), int(len(b) * "9" + len(a) * '0'))
    print("%d/%d" % (x, y))