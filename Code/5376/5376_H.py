import math


def find_gca(a, b):
    while b > 0:
        a, b = b, a % b
    return a


T = int(input())

for tc in range(1, T + 1):
    n = list(map(str, input()))
    cnt_inf, cnt_fin = 0, 0
    for char in range(2, len(n)):
        if n[char] == '(':
            index = char + 1
            while n[index] != ')':
                cnt_inf += 1
                index += 1
        elif n[char] != ')':
            cnt_fin += 1
    cnt_fin -= cnt_inf

    if '(' in n:
        n.pop(n.index('('))
    if ')' in n:
        n.pop(n.index(')'))
    number = float(''.join(n))

    if cnt_inf == 0:
        n1, n2 = 10 ** cnt_fin, number * 10 ** cnt_fin

    else:
        n1 = 10 ** (cnt_fin + cnt_inf) - 10 ** (cnt_fin)
        n2 = number * 10 ** (cnt_fin + cnt_inf) - number * 10 ** (cnt_fin)
    n2 = math.ceil(n2)

    gca_num = find_gca(n1, n2)
    x, y = n1 // gca_num, n2 // gca_num

    print(f'{y}/{x}')