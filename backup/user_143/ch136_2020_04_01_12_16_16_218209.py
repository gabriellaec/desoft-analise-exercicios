import random
dado1=random.randint(1, 6)
dado2=random.randint(1, 6)
dado3=random.randint(1, 6)
soma=(dado1+dado2+dado3)
din=10
while din>0:
    soma=(dado1+dado2+dado3)
    print('você tem {0} dinheiros'. format(din))
    dica=input('quer dica?')
    dic=False
    while not dic:
        if dica=='sim' or dica=='não':
            dic=True
        else:
            dica=input('quer dica?')
    while dica=='sim' and din>0:
        num1=int(input('Número'))
        num2=int(input('Número'))
        num3=int(input('Número'))
        number=False
        while not number:
            if num1>1 and num1<13 and num2>1 and num2<13 and num3>1 and num3<13:
                number=True
            else:
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
        print ('você tem {0} dinheiros'. format(din))
        numb=int(input('Número'))
        numberr=False
        while not numberr:
            if numb>1 and numb<13:
                number=True
            else:
                numb=int(input('Número'))
        if numb==soma:
            din+=din*5
            print("Você ganhou o jogo com {0} dinheiros!". format(din))
            din=-1
        else:
            din-=1
            print('errou')
        b=din
    if din==0:
        print('Você perdeu!')
        
