import random
d = 100
i = 0

print("quantidade de dinheiro disponível:",d)

V = int(input("Aposte um valor:"))
while d > 0:
    if V == 0:
        break
    if V > d:
        print("Você não tem dinheiro suficiente.")
        break
    else:
        S = random.randint(0,36)
    
        aposta = input("A aposta é em um número(n) ou paridade(p)?")
    
        if aposta == "n":
            numero = int(input("Digite um número de 1 a 36:"))
            if numero == S:
                ganhou_n = d + V *35
                print(ganhou_n)
            else:
                perdeu_n = d - V
                print(perdeu_n)
    
        if aposta == "p":
            opcao = (input("Você escolhe par(p) ou ímpar(i)?:"))
            if S%2 == 0:
                S = "p"
            if opcao == S:
                X = d + V*35
                print(X)
            else:
                S = "i"
                erro = d - V
                print(erro)