import random

dado1=random.randint(1,10)
dado2=random.randint(1,10)
soma=dado1+dado2

dinheiros=10

#fase de dicas:
n1=int(input('diga um número: '))
n2=int(input('diga outro número maior ou igual ao anterior: '))
if soma<n1:
    print('Soma menor')
elif soma>n2:
    print('Soma maior')
else:
    print('Soma no meio')

#fase de chutes:
print('você tem {0} dinheiros.'.format(dinheiros))
chutes=int(input('quantos chutes deseja comprar? '))
dinheiros-=chutes
while chute>=0:
    tentativa=int(input('qual seu chute? '))
    if tentativa==soma:
        dinheiros+=5*dinheiros
        break
    else:
        chutes-=1
print('Você terminou o jogo com {0} dinheiros'.format(dinheiros))
