import random
dinheiros = 1000
continuar = True
while continuar == True:
    apostar = str(input("Você deseja apostar? (sim/não): "))
    if apostar == "sim":
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma = dado1 + dado2
        adivinharsoma = int(input("Tente adivinhar a soma: "))
        dinheiros -= 30
        if adivinharsoma == soma:
            dinheiros += 50
            print("Parabéns! Você acertou e está com {0} dinheiros".format(dinheiros))
            continuar == True
        else:
            deseja = str(input("Deseja continuar ou desistir? "))
            if deseja == 'desistir':
                continuar == True
            else:
                adivinharsoma = int(input("Tente adivinhar a soma de novo: "))
                dinheiros -= 20
                if adivinharsoma == soma:
                    dinheiros += 50
                    continuar == True
                else:
                    deseja = str(input("Deseja continuar ou desistir? "))
                    if deseja == 'desistir':
                        continuar == True
                    elif deseja == 'continuar':
                        adivinharsoma = int(input("Tente adivinhar a soma de novo: "))
                        dinheiros -= 10
                        if adivinharsoma == soma:
                            dinheiros += 50
                        continuar == True
    elif apostar == "não":
        continuar = False
print("Você terminou a partida com {0} dinheiros".format(dinheiros))