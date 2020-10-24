import random
jogo=True
d=100
while jogo and d>0:
    a1=0
    e=0
    f=0
    print('Você dispoem de {0}'.format(d))
    ap=int(input('Qual o valor da sua aposta? Você tem {0} reais disponiveis: '.format(d)))
    if ap==0:
        jogo=False
    else:
        ta=str(input('Você quer apostar em paridade(p) ou em um numero(n): '))
        if ta=='p':
            n=random.randint(0,36)
            a=str(input('Você quer apostar em um numero par(p) ou impar(i): '))
            if a=='p':
                b=int(input('Me diga um numero par de 2 a 36: '))
                if b==n:
                    d=d+ap
                else: 
                    d=d+ap
            elif a=='i':
                    c=int(input('Me diga um numero impar de 1 a 35: '))
                    if c==n:
                        d=d+ap
                    elif c%2==0:
                        break
                    else:
                        d=d-ap
        elif ta=='n':
            n=random.randint(0,36)
            f+=ap
            d=100-ap
            n2=int(input('Me diga um numero de 1 a 36: '))
            if n2==n:
                g=100+(ap*35)
                print('Parabens você ganhou {0}'.format(g))
            else:
                print('Continue tentando você tem {0}'.format(d))
