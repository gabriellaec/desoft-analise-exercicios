import random
d1=random.randint(1,6)
d2=random.randint(1,6)
d3=random.randint(1,6)
soma= d1+d2+d3

fichas=10
print('voce tem {0} dinheiros'.format(fichas))

vai= True
while vai:
    g=input('quer dica?')
    if g=='sim':
        fichas-=1
        p1=int(input('n'))
        p2=int(input('n'))
        p3=int(input('n'))
        if soma==p1 or soma==p2 or soma==p3:
            print("Está entre os 3")
        else:
            print("Não está entre os 3")
    elif g=='nao':
        vai= False
        print('você tem {0} dinheiros'.format(fichas))
        n=int(input('chute um número'))
            if n!=soma:
                fichas-=1
            elif n==soma:
                fichas*=6
                print("Você ganhou o jogo com {0} dinheiros!".format(fichas)) 
            elif ficha<=0:
                print("Você perdeu!")
