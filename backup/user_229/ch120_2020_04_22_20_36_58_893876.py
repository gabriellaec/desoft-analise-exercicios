import random
dinheiro = 100

while dinheiro > 0:
    x = random.randint(1,36)
    print(x)
    print(dinheiro)
    aposta = float(input("aposte: "))

    if aposta <= 0:
        break

    tipo = input('deseja apostar n/p? ')
    if tipo == 'n':
        valor = int(input("entre 1 e 36: "))
        if valor == x:
            dinheiro += aposta*35
        else:
            dinheiro -= aposta
    
    elif tipo == 'p':
        tipo2 = input('deseja apostar par ou ímpar? (p/i) ')
        p_ou_i = x%2
        if p_ou_i == 0:
            r = 'p'
        else:
            r = 'i'
        if tipo2 == r:
            dinheiro += aposta
        else:
            dinheiro -= aposta
    