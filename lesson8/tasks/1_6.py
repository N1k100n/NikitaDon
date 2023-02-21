def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]
 
n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]
swap_columns(a, i, j)
for g in a:
    for k in g:
        print(k,end=" ")
    print()
