n = int(input())
k = 0
if n % 2 == 0:
    k += 1
while n != 0:
    n =int(input())
    if n % 2 == 0:
        k += 1
print(k-1)
