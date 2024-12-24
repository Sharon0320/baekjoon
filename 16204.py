h,m,s = map(int,input().split(":"))
if(h > 12):
    h = h-12
first = m*60 + h * 60 * 60

h,m,s = map(int,input().split(":"))
if(h > 12):
    h = h-12
second = m*60 + h * 60 * 60

firsth = first / 3600
first = first%3600
firstm = first / 60
first = first%3600
firsts = first
print(firsth)