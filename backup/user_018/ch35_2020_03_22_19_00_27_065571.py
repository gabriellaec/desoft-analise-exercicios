n = int(input('Digite um número: '))
s = 0 
while n != 0:
    s += n 
    n = int(input('Digite um número: '))
else: 
    print('A soma é igual a {}'.format(s))