from random import randint
dado1 = randint(1,10)
dado2 = randint(1,10)
soma_dados = dado1 + dado2

dinheiros = 10
print('Você começou o jogo com 10 dinheiros')

#Fase Dica
n1 = int(input('Escolha um número: ')
n2 = int(input('Escolha outro número: ')
if soma_dados < n1:
    print('Soma menor')
elif soma_dados > n2:
    print('Soma maior')
else:
    print('Soma no meio')
         
#Fase Chute
jogo = True
print('Você tem {} dinheiros'.format(dinheiros))
while dinheiros > 0:
    chutes = int(input('Quantos chutes você quer comprar? ')
    dinhero_final = dinheiros - chutes
    chutes = 0
    if chutes > 0 and chutes < dinheiro_final:
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