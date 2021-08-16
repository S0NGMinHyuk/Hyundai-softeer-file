a, b = map(int, input().split(" "))
limit = {}
speed = {}

distance = 0
for _ in range(a):
    i, j = map(int, input().split(" "))
    distance += i
    limit[distance] = j

distance = 0
for _ in range(b):
    i, j = map(int, input().split(" "))
    distance += i
    speed[distance] = j

li_key = sorted(list(limit.keys()))
sp_key = sorted(list(speed.keys()))
li = sp = exceed = 0

while 1:
    try:
        if li_key[li] > sp_key[sp]:
            if speed[sp_key[sp]] - limit[li_key[li]] > exceed:
                exceed = speed[sp_key[sp]] - limit[li_key[li]]
            sp += 1
        elif li_key[li] < sp_key[sp]:
            if speed[sp_key[sp]] - limit[li_key[li]] > exceed:
                exceed = speed[sp_key[sp]] - limit[li_key[li]]
            li += 1
        else:
            if speed[sp_key[sp]] - limit[li_key[li]] > exceed:
                exceed = speed[sp_key[sp]] - limit[li_key[li]]
            sp += 1
            li += 1
    except:
        print(exceed)
        break