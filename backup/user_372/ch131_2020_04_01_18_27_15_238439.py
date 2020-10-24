import random
x=random.randint(2,20)
dinheiro=10
#Fase dos chutes
chute1=int(input('Escolha um número de 2 a 20: '))
chute2=int(input('Escolha outro número de 2 a 20: '))
if x>chute1 and x>chute2:
    print('Soma maior')
elif x<dica1 and x<dica2:
    print('Soma menor')
else:
    print('Soma no meio')
#Fase do jogo
print(dinheiro)
numero_de_chutes=int(input('Quantos chutes você deseja comprar(máximo=10)? '))
dinheiro-=numero_de_chutes
acertou=False
while numero_de_chutes>0 or acertou == False:
    tentativa=int(input('Escolha um número de 2 a 20: '))
    if tentativa!=x:
        print('Você errou.')
        numero_de_chutes-=1
    else:
        acertou=True
#Final do jogo
y=numero_de_chutes*5
print('Você terminou o jogo com {0} dinheiros'.format(y))



        
    

    