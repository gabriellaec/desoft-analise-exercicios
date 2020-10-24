import random

#Fase de dicas
d1 = random.randint(1, 10)
d2 = random.randint(1, 10)
s = d1+d2
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if s<n1:
    print('Soma menor')
elif s>n2:
    print('Soma maior')
else:
    print('Soma no meio')