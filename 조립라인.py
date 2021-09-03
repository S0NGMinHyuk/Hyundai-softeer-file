import sys
N = int(sys.stdin.readline())
time = [0, 0]
# N = 작업장 갯수, time = A, B 작업장이 마지막일 경우의 최소 작업 시간

for i in range(N -1):
    aTime, bTime, aTob, bToa = map(int, sys.stdin.readline().split())
    temp = time[0]
    # 14번 줄에서 현재의 time[0] 값이 필요하지만 11번 줄에서 temp[0] 값을 변경하기 때문에 temp 변수에 time[0] 값 임시저장
    
    time[0] = min(aTime +time[0], bTime +bToa +time[1])
    # A작업장 시간 + A작업장이 마지막이었던 경우의 시간 vs B작업장 시간 + B작업장이 마지막이었던 경우의 시간 + B작업장에서 A작업장 오는 시간
    # 더 작은 값을 temp[0] 에 저장
    time[1] = min(bTime +time[1], aTime +aTob +temp)
    # 위와 동일, temp = time[0]
else:
    aTime, bTime = map(int, sys.stdin.readline().split())
    time[0] += aTime ; time[1] += bTime
    # 마지막 작업장의 경우, 이동을 고려하지 않으므로 각 작업장에 작업시간만 추가

print(min(time))
# time 리스트의 최소값 출력