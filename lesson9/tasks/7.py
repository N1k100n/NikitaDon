n = int(input())
a = set(input().split())
b = set(i for i in range(n))
while 'HELP' not in a:
    x = input()
    if x == 'YES':
        b &= a
    else:
        b -= a
    a = set(input().split())
b.discard(n)
print(*sorted(b, key = int))
