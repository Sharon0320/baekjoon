import sys
count = 0
count = int(count)
while(True):
    count +=1
    a,b,c = map(int,sys.stdin.readline().split())
    if(a == 0 and b == 0 and c == 0):
        break
    elif(a == -1):
        if(b>=c):
            print('Triangle #{}\nImpossible.\n'.format(count))
            continue
        br = b**2
        cr = c**2
        ar = (cr - br)**(1/2)
        print('Triangle #{}\nc = {:.3f}\n'.format(count,ar))
    elif(b == -1):
        if(a>=c):
            print('Triangle #{}\nImpossible.\n'.format(count))
            continue
        ar = a**2
        cr = c**2
        br = (cr - ar)**(1/2)
        print('Triangle #{}\nc = {:.3f}\n'.format(count,br))
    elif(c == -1):
        ar = a**2
        br = b**2
        cr = (ar + br)**(1/2)
        print('Triangle #{}\nc = {:.3f}\n'.format(count,cr))