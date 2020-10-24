import random
fichas = 100
print("Você tem {0} fichas.".format(fichas))
aposta = int(input("Quantas fichas deseja aposta? "))

while fichas > 0 and aposta != 0:
    numero = random.randint(0,36)
    print(numero) #apagar
    tipo = input("Escolha o tipo de aposta: número ou paridade.(n/p) ")
    if tipo == "n":
        pn = int(input("Qual o número escolhido? "))
        if pn == numero:
            fichas = aposta * 35 + fichas
        elif pn != numero:
            fichas = fichas - aposta
    if tipo == "p":
        pp = input("Par ou ímpar. (p/i) ")
        if pp == "p":
            if numero%2==0:
                fichas = aposta + fichas
            elif numero%2!=0:
                fichas = fichas - aposta
        elif pp == "i":
            if numero%2==0:
                fichas = fichas - aposta
            elif numero%2!=0:
                fichas = aposta + fichas
    print("Você tem {0} fichas.".format(fichas))
    if fichas > 0:
        aposta = int(input("Quantas fichas deseja aposta? "))