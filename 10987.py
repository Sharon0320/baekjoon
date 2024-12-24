n = list(input())
vowel = []
for i in range(len(n)):
    if (n[i] == 'a' or n[i] == 'e' or n[i] == 'i' or n[i] == 'o' or n[i] == 'u'):
        vowel.append(n[i])
print(len(vowel))