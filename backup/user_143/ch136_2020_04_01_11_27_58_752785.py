import random
dado1=random.randint(1, 6)
dado2=random.randint(1, 6)
dado3=random.randint(1, 6)
soma=(dado1+dado2+dado3)
din=10
while din>0:
    print('você tem {0} dinheiros'. format(din))
    dica=input('quer dica?')
    while dica=='sim':
        num1=int(input('Número'))
        num2=int(input('Número'))
        num3=int(input('Número'))
        if soma==num1 or soma==num2 or soma==num3:
            print('Está entre os 3')
            din-=1
            dica!='sim'
        else:
            print('Não está entre os 3')
            din-=1
            dica=input('quer dica?')
    b=1
    while b>0:    
        numb=int(input('Número')
        print ('você tem {0} dinheiros'. format(din))
        if numb==soma:
            din+=din*5
            print("Você ganhou o jogo com {0} dinheiros!". format(din))
            din=0
            b=0
        else:
            din-=1
            print('Você perdeu!')
            b=din
    

