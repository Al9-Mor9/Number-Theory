number = input()                # 30의 배수인지 확인해볼 숫자

if '0' not in number:           # 만약 해당 숫자에 0이 포함되어 있지 않다면 조건 탈락
    print(-1)

else:
    number_sum = 0              # 숫자들의 각 자리 수를 모두 더해준다
    for i in range(len(number)):
        number_sum += int(number[i])
    if number_sum % 3 != 0:     # 만약 숫자들을 모두 더해준 값이 3으로 나누어 떨어지지 않는다면
        print(-1)               # 배수 판정법의 조건에 맞지 않는 것이다
    else:                       # 위 조건들을 모두 통과했다면 30의 배수이다
        tmp_number = sorted(number, reverse=True) # 가장 큰 값을 찾아야 하기 때문에 내림차순 정렬해주고
        answer = ''.join(tmp_number) # 해당 숫자를 하나로 이어주기
        print(answer)