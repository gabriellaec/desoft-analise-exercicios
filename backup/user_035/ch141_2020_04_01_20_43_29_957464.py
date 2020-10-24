import random
dinheiros = 1000
jogo = True
while jogo and dinheiros != 0:
    resposta_1 = input("Você quer apostar")
    if resposta_1 == "não":
        jogo = False
    elif:
        dado_1 = random.randint(1, 6)
        dado_2 = random.randint(1, 6)
        soma = dado_1 + dado_2
        dinheiros = dinheiros - 30
        resposta_2 = int(input("Chute a soma dos dados")
        if resposta_2 == soma:
            dinheiros = dinheiros + 50
            continue
        elif resposta_2 != soma:
            resposta_3 = input("Quer continuar tentando? ")
            if resposta_3 == "desistir":
                continue
            else:
                dinheiros = dinheiros - 20
                resposta_4 = int(input("Chute a soma dos dados")
                if resposta_4 == soma:
                    dinheiros = dinheiros+50
                elif resposra_4 != soma:
                    print(dado_1)
                    resposta_5 = input("Quer continuar tentando? ")
                    if resposta_5 == "desistir":
                        continue
                    elif resposta_5 == "continuar":
                        dinheiros = dinheiros - 10
                        resposta_6 = int(input("Chute a soma dos dados")
                        if resposta_6 == soma:
                            dinheiros = dinheiros+50
                        elif resposta_6 != soma:
                            continue
print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                                         