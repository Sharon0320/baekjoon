import sys

n = int(input())
unsortedlist = []
for i in range(n):
    inputNum = int(sys.stdin.readline())
    unsortedlist.append(inputNum)
unsortedlist.sort()
for a in unsortedlist:
    print(a)