import random
r=random.randint(2,19)
dinheiro=10
while dinheiro>0:
    print ('você tem {0} dinheiros'.format(dinheiro))
    dicas = input('você quer dicas?(sim/não) ')
    if dicas == 'sim':
        dinheiro = dinheiro - 1
        x = int(input('escolha um número: '))
        y = int(input('escolha um número: '))
        z = int(input('escolha um número: '))
        if x==r or y==r or z==r:
            print('Está entre os 3')
        else:
            print ('Não está entre os 3')
    elif dicas == 'não':
        print ('você tem {0} dinheiros'.format(dinheiro))
        while dinheiro>0:
            chute = int(input('chute um número: '))
            if chute == r:
                dinheiro = dinheiro + 5*dinheiro
                print('Você ganhou o jogo com {0} dinheiros!'.format(dinheiro))
            else:
                dinheiro = dinheiro - 1
                print ('Você perdeu!')
                        
        
    
    