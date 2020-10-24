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

#Fase de chutes
di = 10
qc = int(input('Quantos chutes você gostaria de comprar?'))
chute = int(input('Chuve um valor para a soma: '))
while chute!=s:
    chute = int(input('Chuve um valor para a soma: '))