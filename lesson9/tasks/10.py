n, k = [int(x) for x in input().split()]
days = set()
for i in range(k):
    begin, step = [int(x) for x in input().split()]
    days |= {x for x in range(begin, n+1, step) if x % 7 not in [0, 6]}
print(len(days))
