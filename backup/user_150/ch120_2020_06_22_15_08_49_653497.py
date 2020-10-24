import random

dinheiro = 100

while dinheiro > 0:
    sorteio = random.randint(1, 36)

    print("Você tem {0} dinheiros".format(dinheiro))
    valor = float(input("Quanto você quer apostar? \n"))
    aposta = input("Sua aposta é um número (digite n) ou uma paridade (digite p)?")

    if aposta == "n":
        numero = input("Digite um número entre 1 e 36: ")
        if numero == sorteio:
            dinheiro += 35 * valor
        else:
            dinheiro -= valor

    elif aposta == "p":
        paridade = input("Digite 'p' se você acha que o número é par, ou 'i' se você acha que o número é ímpar")
        if sorteio % 2 == 0 and paridade == 'p':
            dinheiro += valor
        elif sorteio % 2 != 0 and paridade == 'i':
            dinheiro += valor
        else:
            dinheiro -= valor