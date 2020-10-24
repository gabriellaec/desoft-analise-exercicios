a = []
b = input('Digite uma palavra')
i = 0

while b != 'fim':
    a.append(b)
    b = input('Digite uma palavra')
while i < len(a):
    c = a[i]
    if len(c) >= 1 and c[0] == 'a':
        print(b)
    i = i + 1