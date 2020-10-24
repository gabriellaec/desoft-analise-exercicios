import random
n=random.randint(0,36)
jogo=True
while jogo:
    d=100
    a1=0
    e=0
    f=0
    ta=str(input('Você quer apostar em paridade(p) ou em um numero(n): '))
    while ta=='p' and d>0:
        ap=int(input('Qual o valor da sua aposta? Você tem {0} reais disponiveis: '.format(d)))
        if ap==0:
            jogo=False
        a=str(input('Você quer apostar em um numero par(p) ou impar(i): '))
        e+=ap
        d=100-e
        g1=d+ap
        if a=='p':
            b=int(input('Me diga um numero par de 2 a 36: '))
            if b==n:
                print('Você ganhou {0}'.format(g1))
            elif b%2!=0:
                print('Isso não é um numero par.')
            else: 
                print('Continue tentando, você ainda dispoem de {0}'.format(d))
        elif a=='i':
                c=int(input('Me diga um numero impar de 1 a 35: '))
                ap=int(input('Qual o valor da sua aposta? Você tem {0} reais disponiveis: '.format(d)))
                f+=ap
                d=100-f
                an2=100+f
                if c==n:
                    print('Parabens você ganhou {0}'.format(an2))
                ap=int(input('Qual o valor da sua aposta? Você tem {0} reais disponiveis: '.format(d)))
        else:
            if d<=0:
                print('Acabou seu dinheiro')
                jogo=False
    while ta=='n' and d>0:
        ap=int(input('Qual o valor da sua aposta? Você tem {0} reais disponiveis: '.format(d)))
        f+=ap
        d=100-ap
        n2=int(input('Me diga um numero de 1 a 36: '))
        if n2==n:
            g=100+(ap*35)
            print('Parabens você ganhou {0}'.format(g))
        elif n2!=n:
            print('Continue tentando você tem {0}'.format(d))
        else:
            if d==0:
                print('Acabou o dinheiro')
                jogo=False
