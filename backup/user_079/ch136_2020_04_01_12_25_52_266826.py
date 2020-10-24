from random import randint
game = True
while game:
    dado1=randint(1,6)
    dado2=randint(1,6)
    dado3=randint(1,6)
    
    summy = dado1+dado2+dado3

    bag = 10
    
    soap=True
    while soap:
        print('o valor da bag é' ,bag)
        if bag <=0:
            print('Game Over')
            soap=False
            game=False
        else:
            price = True
            while price:
                dica=input('quer dica (sim/não)?: ')
                if dica == 'sim':
                    bag=bag-1
                    n1=int(input('numero?: '))
                    n2=int(input('numero?: '))
                    n3=int(input('numero?: '))
                    if summy == n1:
                        print('Está entre os 3')
                        price=False
                    elif summy == n2:
                        print('Está entre os 3')
                        price=False
                    elif summy == n3:
                        print('Está entre os 3')
                        price=False
                    elif summy != n1:
                        print('Não está entre os 3')
                        price=False
                    elif summy != n2:
                        print('Não está entre os 3')
                        price=False
                    elif summy != n3:
                        print('Não está entre os 3')
                        price=False                    
                if dica == 'não':
                    print(bag)
                    if bag <=0:
                        print('Game Over')
                        break
                    else:
                        roach=True
                        while roach:
                            chute=int(input('chute?:'))
                            if chute == summy:
                                bag = bag + bag*5
                                print('Você ganhou o jogo com', bag ,'dinheiros!')
                                roach=False
                                price=False
                                soap=False
                                game=False
                                
                            else:
                                bag=bag-1
                                print('o valor da bag é' ,bag)
                            if bag <=0:
                                print('Você perdeu!')
                                roach=False
                                price=False
                                soap=False
                                game=False
 
                            