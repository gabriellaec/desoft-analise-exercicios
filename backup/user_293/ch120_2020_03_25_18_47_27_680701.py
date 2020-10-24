import random
dinheiro = 100
while dinheiro != 0:
    print(dinheiro)
    p = int(input("Aposte um valor: "))
    if p != 0:
        per = input("numero('n') ou paridade('p'): ")
        if per == "n":
            aleatorio1 = random.randint(1,36)
            n = int(input("digite um numero: "))
            if n == aleatorio1:
                dinheiro = dinheiro + 35*p
            else:
                dinheiro = dinheiro - p
        elif per == "p":
            aleatorio2 = random.randint(0,36)
            par = aleatorio2 % 2 == 0
            p_i = input("Par ou Impar('p' ou 'i'): ")
            if p_i == "p":
                if par == True:
                    dinheiro = dinheiro + p
                else:
                    dinheiro = dinheiro - p
            elif p_i == "i":
                if par == False:
                    dinheiro = dinheiro + p
                else:
                    dinheiro = dinheiro - p
    else:
        break