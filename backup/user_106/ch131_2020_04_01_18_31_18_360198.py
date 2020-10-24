import random

d1=random.randint(1,10)
d2=random.randint(1,10)
soma=d1+d2

dinheiros=10

a=input('Digite um número: ')
b=input('Digite outro número maior ou igual ao anterior: ')
if soma<a:
    print('Soma menor')
elif soma>b:
    print('Soma maior')
else:
    print('Soma no meio')
    
print(dinheiros)
z=int(input('Quantos chutes quer comprar? '))
dinheiros-=z

while z>0:
    z-=1
    c=int(input('Qual é a soma?'))
    if chute==soma:
        