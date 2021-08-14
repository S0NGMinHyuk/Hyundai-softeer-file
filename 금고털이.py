bag, times = map(int, input().split(" "))
jewelry = {}

for _ in range(times):
    a, b = map(int, input().split(" "))
    if b in jewelry:
        jewelry[b] += a
    else:
        jewelry[b] = a

value = list(jewelry.keys())
value.sort(reverse=True)

price = 0
for i in value:
    if jewelry[i] <= bag:
        price += i*jewelry[i]
        bag -= jewelry[i]
    else:
        price += i*bag
        break
print(price)