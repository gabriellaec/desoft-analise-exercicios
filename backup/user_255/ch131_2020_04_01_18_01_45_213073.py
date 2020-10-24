from random import randint
x=randint(2,20)
dinheiro=10
y=dinheiro
a=int(input('Escolha um numero de 2 a 20:  '))
b=int(input('Escolha outro numero de 2 a 20:  '))
if a>x:
    print('Soma menor')
elif b<x:
    print('Soma maior')
else:
    print('Soma no meio')
print ('Quantidade de dinheiro: {0}'.format(y))
c=int(input('Quantos chutes voce quer comprar?  '))
y-=c
while c>0:
    d=int(input('Qual o seu chute?  '))
    if d==x:
        y=(y-c)*5+(y-c)
    c-=1
print('Você terminou o jogo com {0} dinheiros'.format(y))