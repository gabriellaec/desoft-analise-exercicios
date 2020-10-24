import random

dinheiros = 1000

a=input("Jogo iniciado. Você quer apostar?")

while a != "não":

    dinheiro -= 30

    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)

    b= input("Os dados foram lançados. Chute o valor da soma por 30 dinheiros.")

    if b == dado1 + dado2:
        dinheiros += 50
        print ("Você ganhou 20 dinheiros!")
        print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
        a = ("Você quer iniciar uma nova partida?")
    
    else:
        c = input ("Você quer continuar apostando ou desistir? Se quiser apostar, tente novamente o valor da soma por 20 dinheiros.")
        if c == "desistir":
            a = input("Jogo iniciado. Você quer apostar?")
        else:
            dinheiros -= 20
            if c == dado1 + dado2:
                dinheiros +=50
                print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
            else:
                d = ("Um dos dados apontou {}. Você deseja continuar tentando ou desistir?".format(dado1))
                if d=="desistir":
                    a = "Jogo iniciado. Você quer apostar?"
                if d=="continuar":
                    e = input("Então tente novamente. Isso lhe custara mais 10 dinheiros. ")
                    dinheiros -=10
                    if e==dado1+dado2:
                        dinheiros +=50
                        print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                        a = "Jogo iniciado. Você quer apostar?"

if a == "não":
    print('Você terminou a partida com {0} dinheiros'.format(dinheiros))