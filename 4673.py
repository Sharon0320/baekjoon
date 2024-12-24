list = list(range(1,10001))
for i in range(1,10001):
    result = 0
    result = int(result)
    result += i
    result += i // 10000
    result += i // 1000
    result += (i % 1000) // 100
    result += ((i % 1000) % 100) // 10
    result += (((i % 1000) % 100) % 10)
    if (result in list):
        list.remove(result)
    else:
        continue
for i in list:
    print(i)