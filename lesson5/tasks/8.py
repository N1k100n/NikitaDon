n = int(input())
sum = 0
proizv_factorial = 1
for i in range(1, n+1):
    proizv_factorial *= i
    sum += proizv_factorial
print(sum)
