import random
dinheiro = 100
print (dinheiro)
while dinheiro>0:
    aposta = float(input("Insira o valor da aposta: "))
    if aposta<=0:
        break
    while aposta > dinheiro:
        print("Você não tem dinheiro suficiente para fazer esta aposta!")
        aposta = float(input("Insira o valor da aposta: "))
    tipo_de_aposta = input("A aposta será em um número ou em uma paridade? ")
    if tipo_de_aposta == "n":
        aposta_n = int(input("Escolha um número de 1 a 36 para apostar: "))
        num_random = random.randint(0,36)
        if aposta_n == num_random:
            dinheiro += (35*aposta)
            print (dinheiro)
        else:
            dinheiro -= aposta
            print (dinheiro)
    if tipo_de_aposta == "p":
        aposta_p = input("Escolha 'p' para um número par, ou 'n' para um número ímpar ")
        if aposta_p == "p":
            if num_random % 2 == 0:
                dinheiro += aposta
                print (dinheiro)
            else:
                dinheiro -= aposta
                print (dinheiro)
        if aposta_p == "i":
            if num_random % 2 != 0:
                dinheiro += aposta
                print (dinheiro)
            else:
                dinheiro -= aposta
                print (dinheiro)