import random
r1=random.randint(1,6)
r2=random.randint(1,6)
r3=random.randint(1,6)
dinheiro=10
jogo = True
while jogo:
    print ('você tem {0} dinheiros'.format(dinheiro))
    if dinheiro == 0:
        jogo = False
        print ('Você perdeu!')
    else:
        dicas = input('você quer dicas?(sim/não) ')
        while dicas == 'sim':
            dinheiro = dinheiro - 1
            x = int(input('escolha um número: '))
            y = int(input('escolha um número: '))
            z = int(input('escolha um número: '))
            if x==(r1+r2+r3) or y==(r1+r2+r3) or z==(r1+r2+r3):
                print('Está entre os 3')
            else:
                print ('Não está entre os 3')
            dicas = input('você quer dicas?(sim/não) ')
        while dicas == 'não':
            print ('você tem {0} dinheiros'.format(dinheiro))
            chute = int(input('chute um número: '))
            if chute == (r1+r2+r3):
                dinheiro = dinheiro + 5*dinheiro
                print('Você ganhou o jogo com {0} dinheiros!'.format(dinheiro))
            else:
                dinheiro = dinheiro - 1
if dinheiro == 0:
    print ('Você perdeu!')
                        
        
    
    