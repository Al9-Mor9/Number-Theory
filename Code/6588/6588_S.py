import sys
sys.stdin = open('gold_input.txt')

array = [True for i in range(1000001)]

for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False
# 전체 수 만큼 True의 리스트를 생성해준다.
# 2부터 +1씩 해주면서 그 배수에 해당하는 값들을 False로 바꿔준다.
# 그러면 array에는 소수에 해당하는 값만 True 값을 가지고 있기 때문에
# 이후로는 True값을 가졌을 때 원하는 계산을 해주면 된다.

while True:
    n = int(input())

    if n == 0:
        break

    for i in range(3, len(array)):
        if array[i] and array[n-i]:
            print(n, "=", i, "+", n-i)
            break