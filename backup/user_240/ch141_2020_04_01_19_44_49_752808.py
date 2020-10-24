import random
dinheiros = 1000
d1 = 0
d2 = 0
soma = 0
while dinheiros > 0:
    resposta = input('Quer apostar?')
    if resposta == 'não':
        print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
        break
    else:
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        soma = d1 + d2
        resposta = input()
        dinheiros -= 30
        if int(resposta) == soma:
            dinheiros += 50
        else:
            resposta = input('Quer continuar?')
            if resposta != "desistir":
                dinheiros -= 20
                if int(resposta) == soma:
                    dinheiros += 50
                else:
                    print(d1)
                    resposta = input('Quer continuar?')
                    if resposta == "continuar":
                        dinheiros -= 10
                        resposta = input()
                        if int(resposta) == soma:
                            dinheiros += 50
    print('Você terminou a partida com {0} dinheiros'.format(dinheiros))