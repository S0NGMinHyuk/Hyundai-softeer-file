import sys 
N = int(sys.stdin.readline()) 
time = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(N)], key=lambda x:(x[1], x[0])) 
# time = [[0]*2 for _ in range(N)] 
# for i in range(N): 
#     s, e = map(int, sys.stdin.readline().split()) 
#     time[i][0] = s 
#     time[i][1] = e 
# time.sort(key = lambda x: (x[1], x[0])) 
# 위 주석이 3번줄 내용과 같다.

cnt, end_time = 1, time[0][1]
for start, end in time:
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)