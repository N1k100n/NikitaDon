A = set()
spisok = input().split()
for elem in spisok:
    dlin = len(A)
    A.add(elem)
    if len(A) == dlin:
        print('YES')
    else:
        print('NO')