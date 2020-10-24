import random as rd

dinheiro = 1000

while True:
    chute = 0
    quer_apostar = input("O jogador deseja apostar? ")
    if quer_apostar == "não":
        print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
        break
    if dinheiro == 0:
        break
    while True:
        dado_1 = rd.randint(1,6)
        dado_2 = rd.randint(1,6)
        soma = dado_1 + dado_2
        chute = int(input('Qual seu chute? '))
        dinheiro -= 30
        if chute == soma:
            dinheiro += 50
            print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
            break
        print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
        continuar1 = input('Continuar tentando? ')
        if continuar1 == 'desistir':
            print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
            break
        chute = int(input('Qual o novo chute? '))
        dinheiro -= 20
        if chute == soma:
            dinheiro += 50
            print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
            break
        print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
        print(dado_1)
        continuar2 = input('Continuar tentando? ')
        if continuar2 == "desistir":
            print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
            break
        elif continuar2 == "continuar":
            dinheiro -= 10
            chute = int(input('Qual o novo chute? '))
            if chute == soma:
                dinheiro += 50
                print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
        break