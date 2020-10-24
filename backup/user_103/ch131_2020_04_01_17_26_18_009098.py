import random 
dado1=random.randint(1,10)
dado2=random.randint(1,10)
soma=dado1+dado2
dinheiro=10
num1=int(input('digite um numero:'))
num2=int(input('digite um numero maior que o anterior'))
somaaposta=num1+num2
if somaaposta!=soma:
    if soma< num1:
        print('Soma menor')
    if soma> num2:
        print('Soma maior')
    else:
        print('Soma no meio')
    print('Você tem {0}'.format(dinheiro))

chutes=int(input('você quer comprar quantos chutes?'))
dinheiro-=chutes
fasechutes=True
while chutes>0:
    num1=int(input('digite um numero:'))
    num2=int(input('digite um numero maior que o anterior'))
    novasoma=num1+num2
    if novasoma!=soma:
        chutes-=1
    else:
        ganha=dinheiro+5*dinheiro
        print('Você ganhou {0}'.format(ganha))
    if chutes==0:
        print('Você perdeu, o jogo acabou')
        print('Você terminou o jogo com {0}'.format(dinheiros))            
                    
            
            
            
        
            
        
            