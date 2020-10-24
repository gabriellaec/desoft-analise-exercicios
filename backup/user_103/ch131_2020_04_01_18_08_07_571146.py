import random 
dado1=random.randint(1,10)
dado2=random.randint(1,10)
soma=dado1+dado2
dinheiro=10
num1=int(input('digite um numero:'))
num2=int(input('digite um numero maior que o anterior'))
if soma< num1:
    print('Soma menor')
elif soma> num2:
    print('Soma maior')
else:
    print('Soma no meio')
print('Você tem {0}'.format(dinheiro))
    
chutes=int(input('você quer comprar quantos chutes?'))
dinheiro-=chutes
chutescerto=True
while chutescerto and chutes>0:
    soma1=int(input('digite a soma apostada:'))
    if soma1==soma:
        print('Você acertou!')
        dinheiro+=dinheiro*5
        chutescerto=False
    else:
        chutes-=1

print('Você terminou o jogo com {0}'.format(dinheiro))            
          
                    
            
            
            
        
            
        
            