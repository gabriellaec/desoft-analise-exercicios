import random
n=random.randint(0,36)
d=100
a1=0
e=0
f=0
while d>0:
    ap=int(input('Qual o valor da sua aposta? Você tem {0} reais disponiveis: '.format(d)))
    a=str(input('Você quer apostar em um numero par(p) ou impar(i): '))
    e+=ap
    d=100-e
    if a=='p':
        b=int(input('Me diga um numero par de 2 a 36: '))
        if b==n:
            print('Você ganhou {0}')
        else: 
            print('Continue tentando, você ainda dispoem de {0}'.format(d))
    elif a=='i':
            c=int(input('Me diga um numero impar de 1 a 35: '))
            ap=int(input('Qual o valor da sua aposta? Você tem {0} reais disponiveis: '.format(d)))
            f+=ap
            d=100-f
            an2=100+(ap*35)
            if c==n:
                print('Parabens você ganhou {0}'.format(an2))
            ap=int(input('Qual o valor da sua aposta? Você tem {0} reais disponiveis: '.format(d)))
    else:
        if d==0:
            print('Acabou seu dinheiro')
            break
