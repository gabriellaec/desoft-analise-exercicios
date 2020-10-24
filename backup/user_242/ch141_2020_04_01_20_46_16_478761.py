import random
dinheiro=1000
a=True
dinheiro_suficiente = dinheiro>0
while dinheiro_suficiente==True:
    querer_apostar=input("Deseja apostar?: ")
    if querer_apostar=="não":
        print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
        break
    else:
        dado1 = random.randint (1,6)
        dado2 = random.randint (1,6)
        soma = dado1 + dado2
        chute1= int(input("Chute um valor pra soma dos dados, lhe custará 30 dinheiros: "))
        dinheiro = dinheiro - 30
        if chute1==soma:
            dinheiro = dinheiro + 50
            print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
            continue
        else:
            continuar= input ("Deseja continuar ou desistir?: ")
            if continuar=="desistir":
                print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                continue
            else: 
                chute2= int(input("Chute um valor pra soma dos dados, lhe custará 20 dinheiros: "))
                dinheiro = dinheiro - 20
                if chute2==soma:
                    dinheiro = dinheiro + 50
                    print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                else:
                    mostra_1_dado = print ("O valor do dado1 é {0}".format(dado1))
                    continuar= input ("Deseja continuar tentando ou desistir?: ")
                    if continuar=="desistir":
                        print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                        continue
                    else: 
                        chute3= int(input("Chute um valor pra soma dos dados, lhe custará 10 dinheiros: "))
                        dinheiro = dinheiro - 10
                        if chute3==soma:
                            dinheiro= dinheiro + 50
                            print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                        else:
                            print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                            continue
    