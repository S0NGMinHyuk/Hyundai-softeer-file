virus, multi, time = map(int, input().split(" "))
for _ in range(time):
    virus = virus * multi % 1000000007
print(virus)