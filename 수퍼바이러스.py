def duplicate(multi, time):
    if time%2 == 0:
        temp = duplicate(multi, time//2)
        return (temp**2) % 1000000007

    elif time == 1:
        return multi
        
    else:
        temp = duplicate(multi, time//2)
        return (temp**2 * multi) % 1000000007

virus, multi, time = map(int, input().split(" "))
total = duplicate(multi, time*10)
print(virus*total%1000000007)