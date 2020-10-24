import random
numero = random.randint(0,36)
fichas = 100
print("Você tem {0} fichas.".format(fichas))
aposta = int(input("Quantas fichas deseja aposta? "))

while fichas > 0 and aposta != 0:
    tipo = input("Escolha o tipo de aposta: número ou paridade.(n/p) ")
    if tipo == "n":
        pn = int(input("Qual o número escolhido? "))
        if pn == numero:
            fichas = aposta * 35 + fichas
            print("Você tem {0} fichas.".format(fichas))
            aposta = int(input("Quantas fichas deseja aposta? "))
        elif pn != numero:
            fichas = fichas - aposta
            print("Você tem {0} fichas.".format(fichas))
            aposta = int(input("Quantas fichas deseja aposta? "))
    if tipo == "p":
        pp = int(input("Qual o número escolhido? "))
        if pp == numero:
            fichas = aposta + fichas
            print("Você tem {0} fichas.".format(fichas))
            aposta = int(input("Quantas fichas deseja aposta? "))
        elif pp != numero:
            fichas = fichas - aposta
            print("Você tem {0} fichas.".format(fichas))
            aposta = int(input("Quantas fichas deseja aposta? "))