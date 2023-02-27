s = int(input())
mass = []
for i in range(s):
    mass.append(set())
    for j in range(int(input())):
        mass[i].add(input())
evr = set.intersection(*mass)
all = set.union(*mass)
print(len(evr), *sorted(evr), sep = '\n')
print(len(all), *sorted(all), sep = '\n')