import random

dinheiro = 100

while dinheiro > 0:

    pergunta = input("Você deseja jogar? Se sim, aperte qualquer tecla. Se não, digite f. \n")
    if pergunta != 'f':
        sorteio = random.randint(0, 36)

        print("Você tem {0} dinheiros".format(dinheiro))
        valor = float(input("Quanto você quer apostar? \n"))
        aposta = input("Sua aposta é um número (digite n) ou uma paridade (digite p)? \n")

        if aposta == "n":
            numero = int(input("Digite um número entre 1 e 36: "))
            if numero == sorteio:
                print("Você ganhou! :)")
                dinheiro += 35 * valor
            else:
                print("Você perdeu :(")
                dinheiro -= valor

        elif aposta == "p":
            paridade = input("Digite 'p' se você acha que o número é par, ou 'i' se você acha que o número é ímpar: \n")
            if sorteio % 2 == 0 and paridade == 'p' or sorteio % 2 != 0 and paridade == 'i':
                print("Você ganhou! :)")
                dinheiro += valor
            else:
                print("Você perdeu :(")
                dinheiro -= valor
    else:
        exit()