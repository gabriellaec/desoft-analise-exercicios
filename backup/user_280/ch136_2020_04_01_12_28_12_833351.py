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
    chutando = True
    while chutando == True:
        if resposta1 == 'sim':
            chute1 = int(input('Chute um número:'))
            chute2 = int(input('Chute um número:'))
            chute3 = int(input('Chute um número:'))
            if sorteado == chute1 or sorteado == chute2 or sorteado == chute3:
                print('Está entre os 3')
                chutando = False
            else:
                print('Não está entre os 3')
                chutando = True
            caixa -= 1
    if resposta1 == 'não':
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
