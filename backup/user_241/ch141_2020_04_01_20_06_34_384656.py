import random
dinheiros = 1000

pergunta =input('Você quer apostar ?: ')
while dinheiros > 0:  
    if pergunta =='não':
        break
    num=int(input('número que deseja chutar: '))
    dado1 = random.randint(0,6)
    dado2 = random.randint(0,6)
    if num == dado1 + dado2:
        print('Você terminou a partida com {0} dinheiros'.format(dinheiros+20))
        pergunta =input('Você quer apostar ?: ')   
    if num != dado1 + dado2:
        resposta=input('Você errou, quer tentar novamente ou vai desistir ?: ')
        if resposta =='desistir':
            print('Você terminou a partida com {0} dinheiros'.format(dinheiros-30))
            pergunta =input('Você quer apostar ?: ')
        if resposta == 'continuar':   
            num=int(input('número que deseja chutar: '))
            if num == dado1 + dado2:
                print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                pergunta =input('Você quer apostar ?: ')
            if num !=dado1 + dado2:
                print('Valor de um dos dados {0}'.format(dado1))
                resposta=input('Você errou, quer tentar novamente ou vai desistir ?: ')
                if resposta=='desistir':
                    print('Você terminou a partida com {0} dinheiros'.format(dinheiros-50))
                if resposta=='continuar':
                    num=int(input('número que deseja chutar: '))
                    if num != dado1+dado2:
                        print('Você terminou a partida com {0} dinheiros'.format(dinheiros-60))
                        pergunta =input('Você quer apostar ?: ')
                    if num== dado1 + dado2:
                        print('Você terminou a partida com {0} dinheiros'.format(dinheiros-10))
                        pergunta =input('Você quer apostar ?: ')