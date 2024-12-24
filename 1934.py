import math
e = 1
fac = 1
print("n" , "e")
print("-" , "-----------")
for i in range(10):
    if(i == 0):
        print('{} {}'.format(0,1))
        continue
    elif(i == 1):
        print('{} {}'.format(1,2))
        fac *= i
        e += 1/fac
        continue
    elif(i == 2):
        fac *= i
        e += 1/fac
        print('{} {:.1f}'.format(i,e))
    else:
        fac *= i
        e += 1/fac
        print('{} {:.9f}'.format(i,e))
