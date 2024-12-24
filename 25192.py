import sys

t = int(input())
d = []
count = 0
print(d)
for i in range(t):
    n = sys.stdin.readline()
    if(n not in d):
        d.append(n)
        if(n == "ENTER"):
            continue
        count += 1
print(count)