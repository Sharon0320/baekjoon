n = int(input())
registered = []

for i in range(n):
    age, name = input().split()
    registered.append((int(age), i, name))  # (나이, 가입 순서, 이름) 저장

# 나이를 기준으로 정렬, 나이가 같으면 가입 순서를 유지
registered.sort(key=lambda x: (x[0], x[1]))

for age, _, name in registered:
    print(age, name)
