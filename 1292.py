a,b = map(int,input().split())
s = []
add = 1
while(len(s) != b):
    for i in range(add):
        s.append(add)
        if (len(s) == b):
            break
    add += 1
result = 0
for i in range(a-1,b):
    result += s[i]
print(result)