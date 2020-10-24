import random
dinheiros = 100
aposta = 1 
while aposta != 0 and dinheiros != 0:
    print("Dinheiro disponível: {0}".format(dinheiros))
    aposta = int(input("Quanto deseja apostar? "))
    modo = input("A aposta é em número ou paridade?")
    if modo == "n":
        numero_sorte = int(input("Digite um numero(1-36) "))
        secret = random.randint(0,36)
        print(secret)
        if numero_sorte == secret:
            dinheiros = dinheiros + (35 * aposta)
        else:
            dinheiros = dinheiros - aposta
    else:
        modo2 = input("Par ou Impar?")
        if modo2 == "p":
            secret = random.randint(0,36)
            print(secret)
            if secret % 2 == 0:
                dinheiros = dinheiros + aposta
                print(dinheiros)
                print("par")
            else:
                dinheiros = dinheiros - aposta
                print(dinheiros)
                print("Impar")
        elif modo2 == "i":
            secret = random.randint(0,36)
            print(secret)
            if secret % 2 != 0:
                dinheiros = dinheiros + aposta
                print(dinheiros)
                print("par")
            else:
                dinheiros = dinheiros - aposta
                print(dinheiros)
                print("Impar")