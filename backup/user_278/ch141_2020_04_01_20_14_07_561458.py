import random
dinheiro=1000
querer_apostar=input("Deseja apostar?: ")
a=True
dado1 = random.randint (0,6)
dado2 = random.randint (0,6)
soma = dado1 + dado2
while querer_apostar!="não" and a:
    chute1= int(input("Chute um valor pra soma dos dados, lhe custará 30 dinheiros: "))
    dinheiro = dinheiro - 30
    if chute1==soma:
        dinheiro = dinheiro + 50
        a=False
    else:
        continuar= input ("Deseja continuar ou desistir?: ")
        if continuar=="desistir":
            a=False
        else: 
            chute2= int(input("Chute um valor pra soma dos dados, lhe custará 20 dinheiros: "))
            dinheiro = dinheiro - 20
            if chute2==soma:
                dinheiro = dinheiro + 50
                a=False
            else:
                mostra_1_dado = print ("O valor do dado1 é {0}".format(dado1))
                continuar= input ("Deseja continuar tentando ou desistir?: ")
                if continuar=="desistir":
                    a=False
                else: 
                    chute3= int(input("Chute um valor pra soma dos dados, lhe custará 10 dinheiros: "))
                    dinheiro = dinheiro - 10
                    if chute3==soma:
                        dinheiro= dinheiro + 50
                        a=False
                    else:
                        a=False
print ("Você terminou a partida com {0} dinheiros".format(dinheiro))