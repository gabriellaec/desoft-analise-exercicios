import random
r=random.randint(1,18)
dinheiro=10
if dinheiro>0:
    print ('você tem {0} dinheiros'.format(dinheiro))
    dicas = input('você quer dicas?(sim/não) ')
    while dicas == 'sim':
        dinheiro = dinheiro - 1
        x = int(input('escolha um número: '))
        y = int(input('escolha um número: '))
        z = int(input('escolha um número: '))
        if x==r or y==r or z==r:
            print('Está entre os 3')
        else:
            print ('Não está entre os 3')
    while dicas == 'não':
        print ('você tem {0} dinheiros'.format(dinheiro))
        chute = int(input('chute um número: '))
        if chute == r:
            dinheiro = dinheiro + 5*dinheiro
            print('Você ganhou o jogo com {0} dinheiros!'.format(dinheiro))
        else:
            dinheiro = dinheiro - 1
else:
    print ('Você perdeu!')
                        
        
    
    