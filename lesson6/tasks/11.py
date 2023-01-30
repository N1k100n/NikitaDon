first_elem = int(input())
k = 0
while first_elem != 0:
    next = int(input())
    if next != 0 and first_elem < next:
        k += 1
    first_elem = next
print(k)
