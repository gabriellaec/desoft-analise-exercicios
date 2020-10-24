import random
dado1 = random.randint(1 ,6 )
dado2 = random.randint(1 ,6 )
dado3 = random.randint(1 ,6 )
soma = dado1 + dado2 + dado3
fichas=10
print('voce tem {0} fichas'.format(fichas))
dica= input('quer dica?')
vai= True
while vai:
    if dica == 'sim':
        vai = True
        fichas-=1
        p1= int(input('dado'))
        p2= int(input('dado'))
        p3= int(input('dado'))
        if soma==p1 or soma==p2 or soma==p3:
            print('Está entre os 3')
        else:
            print("Não está entre os 3")
    elif dica == 'nao':
        vai= False
print('voce tem {0} fichas'.format(fichas))
chute= True
while chute:
    if fichas<=0:
        print('Você perdeu!')
        chute= False
    else:
        c=int(input("chute um numero"))
        if c==soma:
            fichas*=6
            chute= False
            print("Você ganhou o jogo com {0} dinheiros!".format(fichas)

