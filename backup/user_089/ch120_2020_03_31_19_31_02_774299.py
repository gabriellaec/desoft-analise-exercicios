import random
d = 100

while d > 0:
    print("quantidade de dinheiro disponível:",d)

    V = int(input("Aposte um valor:"))
    if V == 0:
        break
    if V > d:
        print("Você não tem dinheiro suficiente.")
        break
    else:
        S = random.randint(0,36)
    
        C = input("A aposta é em um número(n) ou paridade(p)?")
    
        if C == "n":
            N = int(input("Digite um número de 1 a 36:"))
            if N == S:
                G = d + V *35
                print(G)
            else:
                P = d - V
                print(P)
    
        if C == "p":
            O = (input("Você escolhe par(p) ou ímpar(i)?:"))
            if S%2 == 0:
                S = "p"
            if O == S:
                X = d + V*35
                print(X)
            else:
                S = "i"
                E = d - V
                print(E)