d1,d2,d3 = map(int,input().split())
sum = (d1+d2+d3)/2
a = sum - d3
b = sum - d1
c = sum - d2

if(a<=0 or b <=0 or c <= 0):
    print(-1)
else:
    print(1)
    print('{:.1f} {:.1f} {:.1f}'.format(a,c,b))