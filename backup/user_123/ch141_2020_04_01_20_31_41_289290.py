import random
dinheiro = 1000

while dinheiro >= 30:
    aposta = input("Você quer apostar?(sim/não)")
    if aposta == "não":
        print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
        break
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    som = d1 + d2
    a = input("Escolha um número:")
    if aposta == "sim":
        if a == som:
            dinheiro += 20
            print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
        elif a != som:
            dinheiro += (-30)
            b = input("Você quer continuar tentando ou desistir?")
            c = input("Escolha um número:")
            d3 = random.randint(1,6)
            d4 = random.randint(1,6)
            som2 = d3 + d4
            if b == "continuar tentando" and som2 == c :
                dinheiro += 30
                print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
            elif b == "continuar tentando" and som2 != c :
                dinheiro += (-20)
                print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                print (d3)
                d = input("Você quer continuar tentando ou desistir?")
                if d == "desistir":
                    print('Você terminou a partida com {0} dinheiros'.format(dinheiro))    
                elif d == "continuar tentando":
                    e = ("Escolha o valor do dado")
                    if e == d4:
                        dinheiro += 40
                        print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                    elif e != d4:
                        dinheiro += (-10)
                    print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
            elif b =="desistir":
                print('Você terminou a partida com {0} dinheiros'.format(dinheiro))