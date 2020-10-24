n = []
i = 0
while n[i-1] != 0:
    n[i] = input('Número {}'.format(i))
    i = i + 1
soma = sum(n)
print (soma)