import random
jogo = True

o = 0
dinheiro = 1000
while jogo == True:
    
    um = input("Quer apostar?")
    if quer == "não":
        print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
        break
    else:

        x = random.randint(1,6)
        y = random.randint(1,6)
        o = x+y
        dois = int(input("Qual o valor da soma?"))
        dinheiro = dinheiro - 30
        if dois == o:
            dinheiro = dinheiro + 50
            print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
        else:
            
            tres= input("Quer continuar?")
            if tres== "desistir":
                print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                jogo= True
            else:
                dinheiro = dinheiro - 20
                quatro= int(input("Qual o valor da soma?"))
                if quatro== o:
                    dinheiro = dinheiro + 50
                    print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                else:
                    print(x)
                    
                    cinco= input("Quer continuar?")
                    if cinco == 'desistir':
                        print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                        jogo = True
                    else:
                        dinheiro = dinheiro -10
                        seis = int(input("Qual o valor da soma?"))
                        if seis== o:
                            dinheiro = dinheiro + 50
                            print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                            jogo= True
                        else:
                            print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                            jogo= True
                            