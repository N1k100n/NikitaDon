max = 0
index_of_max = -1
element = -1
k = 0
while element != 0:
    element = int(input())
    if element > max:
        max = element
        index_of_max = k
    k += 1
print(index_of_max)
