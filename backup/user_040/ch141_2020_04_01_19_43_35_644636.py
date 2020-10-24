from math import randint
dinheiro = 1000
programa = True
while programa == True and dinheiro > 0:
    aposta = input("Você quer apostar?(sim/não) ")
    if aposta == "não":
        print ("Você terminou a partida com {0} dinheiros".format(dinheiro))
        programa = False
    else:
        dado1 = randint(1,6)
        dado2 = randint(1,6)
        chute = int(input("Chute um valor: ")
        dinheiro -= 30
        if chute == dado1 + dado2:
            dinheiro += 50
            print ("Você terminou a partida com {0} dinheiros".format(dinheiro))
        else:
            continuidade = input("Você quer continuar na partida?(continuar/desistir) ")
            if continuidade == "desistir":
                print ("Você terminou a partida com {0} dinheiros".format(dinheiro))
            else:
                chute = int(input("Chute um valor: ")
                dinheiro -= 20
                if chute == dado1 + dado2:
                    dinheiro += 50
                    print ("Você terminou a partida com {0} dinheiros".format(dinheiro))
                else:
                    print (dado1)
                    continuidade = input("Você quer continuar na partida?(continuar/desistir) ")
                    if continuidade == "desistir":
                        print ("Você terminou a partida com {0} dinheiros".format(dinheiro))
                    else:
                        chute = int(input("Chute um valor: ")
                        dinheiro -= 10
                        if chute == dado1 + dado2:
                           dinheiro += 50
                 