import random


def jogo(moneys):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    terminou = False

    meh = input("Quer apostar?")

    if meh == "não":
        result = [0, moneys]
        print('Você terminou a partida com {0} dinheiros'.format(moneys))
        return result

        chute = input("chute a soma")
        moneys -= 30

        if chute is soma:
            moneys += 50
            #terminou = True
            print('Você terminou a partida com {0} dinheiros'.format(moneys))
            result = [1, moneys]
            return result

        pergunta = input("Quer continuar tentando?")
        
        if pergunta == "desistir":
            result = [1, moneys]
            print('Você terminou a partida com {0} dinheiros'.format(moneys))
            return result

        tentativa2 = input("Tente denovo")
        moneys -= 20

        if tentativa2 is soma:
            #terminou = True
            moneys += 50
            print('Você terminou a partida com {0} dinheiros'.format(moneys))
            result = [1, moneys]
            return result

        pergunta2 = input("Quer continuar tentando?")
        if pergunta2 == "desistir":
            #terminou = True
            print('Você terminou a partida com {0} dinheiros'.format(moneys))
            result = [1, moneys]
            return result

        tentativa3 = input("Tente denovo")
        moneys -= 10

        if tentativa3 is soma:
            #terminou = True
            moneys += 50
            print('Você terminou a partida com {0} dinheiros'.format(moneys))
            result = [1, moneys]
            return result

        # else:
        #     terminou = True

        # if terminou:
        #     print('Você terminou a partida com {0} dinheiros'.format(moneys))
        #     result = [1, moneys]
        #     return result


money = 1000
again = jogo(money)

while again[0] is 1:
    again = jogo(again[1])