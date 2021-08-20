repeat = int(input())
lectures = []
for _ in range(repeat):
    temp = tuple(map(int, input().split(" ")))
    append = lectures.append
    append(temp)

lectures.sort(key=lambda x: (x[1], x[0]))

classes = 1

end = lectures[0][1]
while 1:
    if len(lectures) == 1:
        break    
    for i in range(len(lectures)):
        if lectures[i][0] >= end:
            end = lectures[i][1]
            lectures = lectures[i:]
            classes += 1
            break
print(classes)