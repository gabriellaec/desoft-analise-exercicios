import random
dinheiros = 1000
k = True
while k:
    per1 = input("Você quer apostar ?")
    if per1 != "não":
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma = dado1 + dado2
        aposta = int(input("Quanto você quer apostar? "))
        dinheiros -= 30
        if aposta == soma:
            dinheiros += 50
            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
        else:
            per2 = input("Você quer continuar tentando? ")
            if per2 == "desistir":
                 print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
            else:
                aposta2 = int(input("Quanto você quer chutar quanto ?"))
                dinheiros -= 20
                if aposta2 == soma:
                    dinheiros += 50
                    print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                else:
                    print(dado1)
                    per3 = input("Quer desistir ou continuar ?")
                    if per3 == "desistir":
                        print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                    if per3 == "continuar":
                        aposta3 = int(input("Quanto você quer chutar"))
                        dinheiros -= 10
                        if aposta3 == soma:
                            dinheiros += 50
                            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
            
    else:
        k = False
print('Você terminou a partida com {0} dinheiros'.format(dinheiros))

    