t = int(input())
a = []
for i in range(t):
    n=input()
    a.append(n)

a = set(a)
a = list(a)

a.sort()
a.sort(key=len)

for i in a:
    print(i)