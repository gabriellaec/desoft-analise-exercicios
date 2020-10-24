from random import randint
x=randint(1,10)
z=randint(1,10)
w=x+z
dinheiro=10
y=dinheiro
a=int(input('Escolha um numero de 2 a 20:  '))
b=int(input('Escolha outro numero de 2 a 20:  '))
if a>w:
    print('Soma menor')
elif b<w:
    print('Soma maior')
else:
    print('Soma no meio')
print ('Quantidade de dinheiro: {0}'.format(y))
c=int(input('Quantos chutes voce quer comprar?  '))
y-=c
while c>0:
    d=int(input('Qual o seu chute?  '))
    if d==w:
        y=(y-c)*5+(y-c)
    c-=1
print('Você terminou o jogo com {0} dinheiros'.format(y))