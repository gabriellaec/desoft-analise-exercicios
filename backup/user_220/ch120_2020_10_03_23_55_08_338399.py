import random
fichas = 100
print("Você tem {0} fichas.".format(fichas))
aposta = int(input("Quantas fichas deseja aposta? "))

while fichas > 0 and aposta != 0:
    numero = random.randint(0,36
    tipo = input("Escolha o tipo de aposta: número ou paridade.(n/p) ")
    if tipo == "n":
        pn = int(input("Qual o número escolhido? "))
        if pn == numero:
            fichas = aposta * 35 + fichas
        elif pn != numero:
            fichas = fichas - aposta
    if tipo == "p":
        pp = int(input("Qual o número escolhido? "))
        if pp == numero:
            fichas = aposta + fichas
        elif pp != numero:
            fichas = fichas - aposta
    if fichas > 0:
        print("Você tem {0} fichas.".format(fichas))
        aposta = int(input("Quantas fichas deseja aposta? "))
 