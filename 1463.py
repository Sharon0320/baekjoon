def cal(n):
    while(n!=1):
        if(n%3==0):
            return cal(n/3)
        elif(n%2==0):
            return cal(n/2)
        else:
            return cal(n-1)
n = int(input())
print(cal(n))