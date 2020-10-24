import random
fichas = 100
print("Você tem {0} fichas.".format(fichas))

while fichas > 0:
    numero = random.randint(0,36)
    aposta = int(input("Quantas fichas deseja aposta? "))
    tipo = input("Escolha o tipo de aposta: número ou paridade.(n/p) ")
    if tipo == "n":
        pn = int(input("Qual o número escolhido? "))
        if pn == numero:
            fichas = aposta * 35 + fichas
            print("Você tem {0} fichas.".format(fichas))
        elif pn != numero:
            fichas = fichas - aposta
            print("Você tem {0} fichas.".format(fichas))
    if tipo == "p":
        pp = int(input("Qual o número escolhido? "))
        if pp == numero:
            fichas = aposta + fichas
            print("Você tem {0} fichas.".format(fichas))
        elif pp != numero:
            fichas = fichas - aposta
            print("Você tem {0} fichas.".format(fichas))
            