import sys
import random


def jogo(moneys):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    terminou = False

    meh = input("Quer apostar?")

    if meh == "não":
        result = moneys
        print('Você terminou a partida com {0} dinheiros'.format(moneys))
        return none

    chute = input("chute a soma")
    moneys -= 30

    if chute is soma:
        moneys += 50
        print('Você terminou a partida com {0} dinheiros'.format(moneys))
        result = moneys
        return result

    pergunta = input("Quer continuar tentando?")

    if pergunta == "desistir":
        result = moneys
        print('Você terminou a partida com {0} dinheiros'.format(moneys))
        return result

    tentativa2 = input("Tente denovo")
    moneys -= 20

    if tentativa2 is soma:
        moneys += 50
        print('Você terminou a partida com {0} dinheiros'.format(moneys))
        result = moneys
        return result

    pergunta2 = input("Quer continuar tentando?")
    if pergunta2 == "desistir":
        print('Você terminou a partida com {0} dinheiros'.format(moneys))
        result = moneys
        return result

    tentativa3 = input("Tente denovo")
    print("o valor do primeiro dado eh {0}".format(dado1))
    moneys -= 10

    if tentativa3 is soma:
        moneys += 50
        print('Você terminou a partida com {0} dinheiros'.format(moneys))
        result = moneys
        return result


money = 1000
money = jogo(money)
#while money > 0:
    #money = jogo(money)