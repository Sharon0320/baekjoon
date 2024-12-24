t = int(input(''))
list = []
for i in range(t):
    n = int(input(''))
    list.append(n)
list.sort()
for i in range(t):
    print(list[i])