import random

dinheiros = 1000
jogo = True
one = input("Você quer apostar?\n")
if one == "não":
    print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
if one != "não":
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        o = x + y
        two = int(input("Qual a soma?\n"))
        dinheiros = dinheiros - 30
        if two == o:
            dinheiros = dinheiros + 50
            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
            jogo = True
        else:
            three = input("Quer continuar ou quer desistir?\n")
            if three == "desistir":
                print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                jogo = True
            else:
                dinheiros = dinheiros - 20
                four = int (input("Qual a soma?\n"))
                if four == o:
                    dinheiros = dinheiros + 50






