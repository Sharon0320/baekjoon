import math
count = 0
t = int(input(''))
m = list(map(int,input('').split(' ')))
for i in range(t):
    if (m[i]):
        count += 1
print(count)