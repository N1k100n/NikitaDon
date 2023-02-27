s = set(i+1 for i in range(int(input())))
while True:
    guess = input()
    if guess == "HELP":
        break
    a = set([int(i) for i in guess.split()])
    if len(s-a) >= len(s)/2:
        print("NO")
        s -= a
    else:
        print("YES")
        s &= a
print(*s)
