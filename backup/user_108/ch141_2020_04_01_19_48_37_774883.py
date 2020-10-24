import random
quer_jogar = True
dinheiro = 1000
while quer_jogar:
    x = input("quer apostar?")
    print(x)
    if x == "não":
        quer_jogar == False
    else:
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        for custo in [30,20,10]:
            
            if custo > 10 and input("quer chutar de novo?") == "desistir":
                break
            elif int(input("chute um numero")) == dado1 + dado2:
                dinheiro+=50
                dinheiro -= custo
                break
            dinheiro -= custo
            
            
            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
         