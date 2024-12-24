t = int(input())
count = 0

for i in range(t):
    n = list(input())
    testlist = []
    for j in range(len(n)):
        if (j == 0):
            testlist.append(n[0])
        else:
            if (n[i-1] == n[i]):
                testlist.append(n[i])
            else:
                if (n[i] not in testlist):
                    testlist.append(n[i])
                else:
                    break
        print(testlist)
    count+=1
print(count)