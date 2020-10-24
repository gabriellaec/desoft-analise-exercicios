import random
d = 100
while d > 0:
    print (f"Você tem R${d}:")
    aposta = int(input("Valor da sua aposta:"))
    if aposta == 0:
        break
    elif aposta > d:
        print ("Você não tem dinheiro para isso")
    else:
        tipo = input("tipo de aposta (n) para numero, (p) para paridade): ")
        if tipo == "n":
            escolha = int(input("Escolha um número de 1 a 36:"))
            p = random.randint(0,36)
            if p == escolha:
                d = d + d*35
            else:
                d = d - aposta
        elif tipo == "p":
            escolha2 = input("Escolha se você quer um número PAR (p) ou número IMPAR (i):")
            p = random.randint(0,36)
            if p%2 == 0:
                p = "p"
            elif p%2 != 0:
                p = "i"
            if escolha2 == p:
                d = d + aposta
            else:
                d = d - aposta