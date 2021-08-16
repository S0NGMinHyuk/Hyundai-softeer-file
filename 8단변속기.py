mission = list(map(int, input().split(" ")))
mix = 0

for i in range(len(mission)-1):
    if mission[i+1] - mission[i] == 1 or mission[i+1] - mission[i] == -1:
        pass
    else:
        mix = 1
        break

if mix:
    print("mixed")    
elif mission[0] == 8:
    print("descending")
else:
    print("ascending")