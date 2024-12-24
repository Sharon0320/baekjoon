n = int(input())
p = list(map(int,input().split()))
p.sort()
least = 0
for i in range(n):
    least = least + p[i]*(n-i)
print(least)