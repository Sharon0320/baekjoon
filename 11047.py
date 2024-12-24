n,k = map(int,input().split())
count = 0
if (k//50000 > 0):
    count += k//50000
    k=k%50000
if (k//10000 > 0):
    count += k//10000
    k=k%10000
if (k//5000 > 0):
    count += k//5000
    k=k%5000
if (k//1000 > 0):
    count += k//1000
    k=k%1000
if (k//500 > 0):
    count += k//500
    k=k%500
if (k//100 > 0):
    count += k//100
    k=k%100
if (k//50 > 0):
    count += k//50
    k=k%50
if (k//10 > 0):
    count += k//10
    k=k%10
if (k//5 > 0):
    count += k//5
    k=k%5
if (k < 4):
    count += k
print(count)