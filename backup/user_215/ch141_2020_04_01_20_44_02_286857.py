import random
dinheiros = 1000
rolando = True
while rolando:
    pergunta_inicial = str(input("Você quer apostar?"))
    if pergunta_inicial == "não":
        print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
        rolando = False
    else:
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma = dado1 + dado2
        chute = int(input("Tente adivinhar a soma"))
        dinheiros -= 30
        if chute == soma:
            print("Parabens voce acertou")
            dinheiros += 50
            continue
        else:
            print("Voce errou")
            pergunta = 0
            while chute != soma and pergunta != soma:
                pergunta = input("Você quer continuar tentando ou desistir?")
                if pergunta == "desistir":
                    print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                    rolando = False
                    break
                else:
                    dinheiros -= 20
                    if pergunta == soma:
                        print("Parabens voce acertou")
                        dinheiros += 50
                        break
                    else:
                        print("Voce errou")
                        continue

