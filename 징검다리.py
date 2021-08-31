import sys
N = int(sys.stdin.readline())
rocks = list(map(int, sys.stdin.readline().split()))
way = [0]*N
# N = 돌의 갯수, rocks = 돌의 높이 리스트
# way = 해당 인덱스의 돌에 갈 때 밟을 수 있는 최대 돌의 갯수용 리스트

for i in range(N):
    temp = 1
    # rocks[i] = 목적지 돌

    for j in range(i):
        if rocks[i] > rocks[j]:
            if way[j] +1 > temp:
                temp = way[j] +1
        # 목적지 돌 전에 목적지 돌의 높이보다 작은 돌이 있다면 
        # 해당 돌의 밟는 돌 갯수 + 1 을 할 값을 temp 값에 저장

    way[i] = temp
    # 최종적으로 가장 큰 temp 값을 way[i] 에 추가

print(max(way))
# way 리스트의 최대값 출력