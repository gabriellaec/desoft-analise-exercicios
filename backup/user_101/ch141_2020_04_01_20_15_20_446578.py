from random import randint

din_inicial = 1000
vont0 = input("Você quer apostar? ")
din = din_inicial

while din > 0:
    if vont0 == "não":
        break
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    palpite0 = int(input("Qual o seu palpite? "))
    if palpite0 == (d1 + d2):
        din += 20
    else:
        din -= 30
        vont1 = input("Quer tentar ou desistir? ")
        if vont1 == "desistir":
            print ('Você terminou a partida com {0} dinheiros'.format(din))
        else:
            din -= 20
            palpite1 = int(input("Qual o seu palpite? "))
            if palpite1 == (d1 + d2):
                din += 50
            else:
                print (d1)
                vont2 = input("Quer tentar ou desistir? ")
                if vont2 == "desistir":
                    print ('Você terminou a partida com {0} dinheiros'.format(din))
                elif vont2 == "continuar":
                    palpite2 = int(input("Qual o seu palpite? "))
                    din -= 10
                    if palpite2 == (d1 + d2):
                        din += 50
                        print ('Você terminou a partida com {0} dinheiros'.format(din))
                    else:
                        print ('Você terminou a partida com {0} dinheiros'.format(din))