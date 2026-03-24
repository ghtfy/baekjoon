A, B = map(int, input().split())
C = int(input())

B += C  # 분에 요리 시간 더하기

A += B // 60  # 넘친 분을 시간으로 변환
B = B % 60    # 분은 60으로 나눈 나머지

A = A % 24    # 24시간 기준으로 맞추기

print(A, B)