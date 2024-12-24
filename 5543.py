a,b = map(int,(input('')).split())
r_a = int(str(a)[::-1])
r_b = int(str(b)[::-1])
print(max(r_a,r_b))