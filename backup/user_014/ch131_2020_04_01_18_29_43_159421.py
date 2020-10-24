from random import randint
dado1 = randint(1,10)
dado2 = randint(1,10)
soma_dados = dado1 + dado2

dinheiro = 10
print('Você começou o jogo com 10 dinheiros')

jogo = True

#Fase Dica
print('Você está na fase dica')

n1= int(input('Escolha um número: ')
n2 = int(input('Escolha outro número: ')
if soma_dados < n1:
    print('Soma menor')
elif soma_dados > n2:
    print('Soma maior')
else:
    print('Soma no meio')
         
#Fase Chute
print('Você tem {} dinheiros'.format(dinheiro))
while jogo:
    while dinheiro > 0: #você pode escolher quantos chutes comprar
        chutes = int(input('Quantos chutes você quer comprar? ')
        dinhero_final = dinheiro - chutes
        if chutes > 0:
            n3 = int(input('Escolha um número: ')
            if n3 == soma_dados:
                dinheiro_ganhado = dinheiros * 3    
                chutes += 1                  
                jogo = False
                print('O jogo acabou e você ganhou {0}'.format(dinheiro_ganhado))
            else:
              n4 = int(input('Escolha outro número: ')
              chutes += 1
        else:
            dinheiro_final = dinheiros - chutes
            jogo = False
            print('Você terminou o jogo com {0} dinheiros'.format(dinheiro_final))  