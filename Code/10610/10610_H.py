import sys
sys.stdin = open('text.txt', 'r')
#####
n = list(input())
_n = []
s = 0
ans = []

for i in n:
    i = int(i)
    _n.append(i)
    s += i

#
if s % 3 or '0' not in n:
    print(-1)
    exit()
n = sorted(n, reverse=True)
print(''.join(n))
