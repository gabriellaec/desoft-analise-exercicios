import random
d1=random.randint(1,10)
d2=random.randint(1,10)
sd=d1+d2
d=10
g=0
a=int(input('Me diga um numero de 1 a 20: '))
a2=int(input('Me diga um numero maior ou igual ao numero anterior: '))
if a<sd:
    print('Soma menor')
elif a2>sd:
    print('Soma maior')
else:
    print('Soma no meio')
print('Voce tem {0} dinheiros'.format(d))
c=int(input('Quantos chutes quer comprar, cada chute custa 1 dinheiro: '))
d=d-c
c2=1
while c>0:
    c2=+1
    c=c-c2
    c1=int(input('Diga seu chute: '))
    g=d+d*5
    if c1==sd:
        print('Você acertou e ganhou {0} dinheiros'.format(g))
        break
    elif c==0:
        print('Você acabou o jogo com {0} dinheiros'.format(d))
    else:
        c1=int(input('Diga seu chute: '))