import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
soma_dado = dado1 + dado2
dinheiro = 1000
print('Você tem {0} dinheiros'.format(dinheiro))
resp = input("Você quer apostar? ")
while resp != 'não':
    chute = int(input("Chute um valor para soma dos dados"))
    if chute> 0:
        dinheiro -= 30
    if chute == soma_dado:
        dinheiro +=50
        print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
        resp = input("Você quer apostar? ")
        if resp == "não":
                break
    else:
        print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
        alt = input("Você quer continuar jogando ou você que desistir?")
        if alt == "desistir":
            resp = input("Você quer apostar? ")
            if resp == "não":
                break
        else:
            print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
            chute2 = int(input("Chute um valor para soma dos dados"))
            if chute2> 0:
                dinheiro -= 20
            if chute2 == soma_dado:
                dinheiro += 50
                print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                resp = input("Você quer apostar? ")
                if resp == "não":
                    break
            else:
                print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                print("O valor de um dos dados é {0}".format(dado1))
                alt2 = input("Você quer continuar jogando ou você que desistir?")
                if alt2 == 'desistir':
                    resp = input("Você quer apostar? ")
                    if resp == "não":
                        break
                elif alt2 == 'continuar':
                    chute3 = int(input("Chute um valor para soma dos dados"))
                    if chute3> 0:
                        dinheiro -= 10
                    if chute3 == soma_dado:
                        dinheiro+=50
                        print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                        resp = input("Você quer apostar? ")
                        if resp == "não":
                            break
                    else:
                        print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                        print("Não deu dessa vez")
                        resp = input("Você quer apostar? ")
                        if resp == "não":
                            break