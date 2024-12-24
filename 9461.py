def triangle(n):
    list = [1,1,1,2,2,3,4,5,7,9]
    if(n <= len(list)):
        return list[n-1]

    for i in range(10,n):
        list.append(list[i-1]+list[i-5])
    return list[-1]

t = int(input())
for i in range(t):
    n = int(input())
    print(triangle(n))