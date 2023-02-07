# 두 숫자를 입력 받아 최대 공약수를 구하는 함수
# b가 0이하가 될 때까지 계속 반복하다가, 조건이 충족되면 a 반환
def calc(a,b) :
    while b > 0 :
        tmp = a % b     
        a = b
        b = tmp
    return a

# 각 자리의 값을 입력 받고, 모든 숫자를 서로 곱해주는 과정
N = int(input())
N_nums = list(map(int,input().split()))
calc_N_nums = 1
for i in N_nums:
    calc_N_nums = (calc_N_nums*i)

# 각 자리의 값을 입력 받고, 모든 숫자를 서로 곱해주는 과정
M = int(input())
M_nums = list(map(int,input().split()))
calc_M_nums = 1
for i in M_nums:
    calc_M_nums = (calc_M_nums*i)

# 두 수가 준비 되었다면 함수를 통해 최대 공약수를 출력해준다
print(calc(calc_N_nums,calc_M_nums))