from math import randint
dinheiros = 1000
programa = True
while programa == True and dinheiros > 0:
    aposta = input("Você quer apostar?(sim/não) ")
    if aposta == "não":
        print ("Você terminou a partida com {0} dinheiros".format(dinheiros))
        programa = False
    else:
        dado1 = randint(1,6)
        dado2 = randint(1,6)
        chute = int(input("Chute um valor: ")
        dinheiros -= 30
        if chute == dado1 + dado2:
            dinheiros += 50
            print ("Você terminou a partida com {0} dinheiros".format(dinheiros))
        else:
            continuidade = input("Você quer continuar na partida?(continuar/desistir) ")
            if continuidade == "desistir":
                print ("Você terminou a partida com {0} dinheiros".format(dinheiros))
            else:
                chute = int(input("Chute um valor: ")
                dinheiros -= 20
                if chute == dado1 + dado2:
                    dinheiros += 50
                    print ("Você terminou a partida com {0} dinheiros".format(dinheiros))
                else:
                    print (dado1)
                    continuidade = input("Você quer continuar na partida?(continuar/desistir) ")
                    if continuidade == "desistir":
                        print ("Você terminou a partida com {0} dinheiros".format(dinheiros))
                    else:
                        chute = int(input("Chute um valor: ")
                        dinheiros -= 10
                        if chute == dado1 + dado2:
                            dinheiros += 50
                            print ("Você terminou a partida com {0} dinheiros".format(dinheiros))
                        else:
                            print ("Você terminou a partida com {0} dinheiros".format(dinheiros))