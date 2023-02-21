a=[int(i) for i in input().split()]
t=a+[0]
b=[int(i) for i in input().split()]
k=b[0]
c=b[1]
for i in range (0, len(t)):
    if i==k:
        t[i:]=[c]+t[i:len(t)]
t.pop()
print(' ' .join(str(i) for i in t))
