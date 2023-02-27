n, m = [int(i) for i in input().split()]
a = set()
b = set()
for i in range(n):
    a.add(int(input()))
for j in range(m):
    b.add(int(input()))
print(len(a & b))
print(*sorted(a & b))
print(len(a - b))
print(*sorted(a - b))
print(len(b - a))
print(*sorted(b - a))
