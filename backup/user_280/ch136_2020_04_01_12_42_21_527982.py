#no vscode dá certinho
import random
a = random.randint(1,6)
b = random.randint(1,6)
c = random.randint(1,6)
sorteado = a + b + c
caixa = 10
jogando = True
while caixa > 0 and jogando==True:
    print('Você tem {} dinheiros'.format(caixa))
    resposta1 = str(input('Você quer uma dica?(não/sim)'))
    if resposta1 == 'sim':
        chute1 = int(input('Chute um número:'))
        chute2 = int(input('Chute um número:'))
        chute3 = int(input('Chute um número:'))
        if sorteado == chute1 or sorteado == chute2 or sorteado == chute3:
            print('Está entre os 3')
        else:
            print('Não está entre os 3')
        caixa -= 1
    else:
        print('Você tem {} dinheiros'.format(caixa))
        if caixa == 0:
            jogando = False
        else: 
            chute4 = int(input('Chute um número:'))
            if chute4 == sorteado:
                caixa += caixa*5
                print ('Você ganhou o jogo com {} dinheiros!'.format(caixa))
                jogando = False
            else:
                caixa -= 1
                print ('Você perdeu!')
jogando = False