import random
dinheiro = 100
while dinheiro != 0:
    print("voce tem {0}, dinheiros".format(dinheiro))
    aposta = float(input("Digite sua aposta: "))
    p_i = input("Voce deseja apostar em paridade'p,i'ou 'n': ")
    if p_i == "n":
        num = int(input("Digite um numero entre 1-36: "))
        a = random.randint(1,36)
        if num == a:
            dinheiro = dinheiro+(aposta*35)
        else:
            dinheiro = dinheiro-aposta
    elif p_i == "p":
        num = int(input("Digite um numero entre 1-36: "))
        a = random.randint(1,36)
        if num % 2 == 0:
            dinheiro = dinheiro+aposta
        else:
            dinheiro = dinheiro-aposta
            break
    elif p_i == "i":
        num = int(input("Digite um numero entre 1-36: "))
        a = random.randint(1,36)
        if num % 2 != 0:
            dinheiro = dinheiro+aposta
        else:
            dinheiro = dinheiro-aposta
            break