import random 
dinheiro=1000

while dinheiro>0:
    aposta= input("você deseja jogar? (sim/não)")
    dado1= random.randrange(1,7)
    dado2= random.randrange(1,7)
    soma_dados=dado1+dado2
    if aposta =="sim":
        chute= int(input("chute um numero(isso lhe custará 30 dinheiros"))
        if soma_dados=="chute":
            dinheiro+=20
        elif soma_dados != "aposta": 
            continuar_jogando= input("deseja continuar jogando ou deseja desistir? ")
            if continuar_jogando=="desistir":
                dinheiro=dinheiro
            elif continuar_jogando != "desistir":
                sequencia=input("digite aqui uma sequencia de números para tentar aceitar a soma, isso lhe custará 20 dinheiros" )
                if sequencia == soma_dados:
                    dinheiro+=50 
                else: 
                    print("o valor de um dos dados é {0}".format(dado1))
                    continuar_tentando=input("deseja continuar tentado acertar ou deseja desistir?(disistir/continuar) ")
                    if continuar_tentando=="desistir":
                        aposta=="sim"
                    if continuar_tentando=="continuar":
                        pergunta = int(input("digite na sequência um número para tentar acertar e isso lhe custa mais 10 dinheiros")
                        if soma_dados=="pergunta":
                            dinheiro-=10
        print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
        else:
            break
                                       
        