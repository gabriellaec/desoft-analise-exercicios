n = []
i = 1
n[0] = input('Número 1: ')
while n[i-1] != 0:
    n[i] = input('Número {}'.format(i+1))
    i = i + 1
soma = sum(n)
print (soma)