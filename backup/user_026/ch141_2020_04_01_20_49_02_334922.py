import random
saldo=1000
a=True
dinheiro_necessario = dinheiro>0
while dinheiro_necessario==True:
    querer_apostar=input("Deseja apostar?: ")
    if querer_apostar=="não":
        print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
        break
    else:
        dado1 = random.randint (1,6)
        dado2 = random.randint (1,6)
        soma = dado1 + dado2
        chute1= int(input("Chute um valor pra soma dos dados, lhe custará 30 dinheiros: "))
        saldo = saldo - 30
        if chute1==soma:
            saldo = saldo + 50
            print('Você terminou a partida com {0} dinheiros'.format(saldo))
            continue
        else:
            continuar= input ("Deseja continuar ou desistir?: ")
            if continuar=="desistir":
                print('Você terminou a partida com {0} dinheiros'.format(saldo))
                continue
            else: 
                chute2= int(input("Chute um valor pra soma dos dados, lhe custará 20 dinheiros: "))
                saldo = saldo - 20
                if chute2==soma:
                    saldo = saldo + 50
                    print('Você terminou a partida com {0} dinheiros'.format(saldo))
                else:
                    mostra_1_dado = print ("O valor do dado1 é {0}".format(dado1))
                    continuar= input ("Deseja continuar tentando ou desistir?: ")
                    if continuar=="desistir":
                        print('Você terminou a partida com {0} dinheiros'.format(saldo))
                        continue
                    else: 
                        chute3= int(input("Chute um valor pra soma dos dados, lhe custará 10 dinheiros: "))
                        saldo = saldo - 10
                        if chute3==soma:
                            saldo= saldo + 50
                            print('Você terminou a partida com {0} dinheiros'.format(saldo))
                        else:
                            print('Você terminou a partida com {0} dinheiros'.format(saldo))
                            continue