import random as rnd
dinheiro = 100

while dinheiro > 0:
    sorteio = rnd.randint(0,36)
    print(dinheiro)
    aposta = input()

    if aposta == 0:
        break
    num_ou_par = input()
    if num_ou_par == 'n':
        num = input()
        sorteio = rnd.randint(0,36)
        if num == sorteio:
            dinheiro += aposta*35
        else:
            dinheiro -= aposta

    elif num_ou_par == 'p':
        par = input()
        sorteio = rnd.randint(0,36)
        if par == 'p' and sorteio% == 0:
            dinheiro += aposta
        elif par == 'i' and sorteio%2 != 0: 
            dinheiro += aposta
        else:
            dinheiro -= aposta