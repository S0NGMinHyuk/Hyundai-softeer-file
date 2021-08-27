import sys
student, cycle = map(int, sys.stdin.readline().split())
score = list(map(int, sys.stdin.readline().split()))
# student = 학생 수, cycle = 평균 구할 횟수, score = 학생들의 성적 리스트

for _ in range(cycle):
    a, b = map(int, sys.stdin.readline().split())
    # 성적을 더할 범위 a, b 를 받음

    total = 0
    for i in range(a-1, b):
        total += score[i]
    # total = a, b 사이의 성적 합

    total = total / (b -a +1)
    print("%.2f" % total)
    # total 값이 평균이 되도록 나누고 소수점 3자리에서 반올림과 출력