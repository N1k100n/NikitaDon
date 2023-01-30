n = -1
x = int(input())
i2 = 1
i1 = 1
while n != 0:
    n = int(input())
    if x == n:
        i1 += 1
    elif i2 < i1:
        i2 = i1
        i1 = 1
    else:
        i1 = 1
    x = n
print(i2)
