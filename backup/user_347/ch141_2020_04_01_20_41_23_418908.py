import random

dinheiros = 1000
while dinheiros > 0:
    one = input("Você quer apostar?\n")
    if one == "não":
        print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
        break
    else:
            x = random.randint(1, 6)
            y = random.randint(1, 6)
            o = x + y
            two = int(input("Qual a soma?\n"))
            dinheiros = dinheiros - 30
            if two == o:
                dinheiros = dinheiros + 50
                print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
            else:
                three = input("Quer continuar ou quer desistir?\n")
                if three == "desistir":
                    print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                    continue
                else:
                    four = int (input("Qual a soma?\n"))
                    dinheiros = dinheiros - 20
                    if four == o:
                        dinheiros = dinheiros + 50
                        print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                    else:
                        print (x)
                        five = input("Sabendo um dado, quer continuar ou desistir?\n")
                        if five == "desistir:
                            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                            continue
                        if
                        