import random
quer_jogar = True
dinheiro = 1000
while quer_jogar:
    if input("quer apostar?") == "não":
        quer_jogar == false
    else:
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        for custo in [30,20,10]:
            dinheiro -= custo
            if int(inpunt("chute um numero")) == dado1 + dado2:
                dinheiro+=50
                break
            elif custo > 10 and input("quer chutar de novo?") == "desistir":
                break
            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
         