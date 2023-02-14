for _ in range(3):
    number = int(input())               # 숫자 입력 받기
    answer = '1'                        # 1로 시작해서 조건문이 충족되지 않는다면 1을 추가해주기 위해 str 형태로 저장
    while True:
        if int(answer) % number == 0:   # 1로만 이루어진 숫자가 조건에 충족된다면 answer의 길이를 반환하고 반복문 종료
            print(len(answer))
            break
        else:
            answer += '1'               # 만약 1로 나누어 떨어지지 않는다면 answer에 1씩 추가