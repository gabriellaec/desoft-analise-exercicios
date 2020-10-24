import random
dinheiro = 100
print (dinheiro)
while dinheiro>0:
    #num_random = random.randint(0,36)
    aposta = float(input("Insira o valor da aposta: "))
    while aposta > dinheiro:
        print("Você não tem dinheiro suficiente para fazer esta aposta!")
        aposta = float(input("Insira o valor da aposta: "))
    tipo_de_aposta = input("A aposta será em um número ou em uma paridade? ")
    if tipo_de_aposta == "n":
        num_random = random.randint(1,36)
        aposta_n = int(input("Escolha um número de 1 a 36 para apostar: "))
        if aposta_n == num_random:
            dinheiro += (35*aposta)
            print ("Parabéns você ganhou!)
            print("Agora você tem um saldo de " + str(dinheiro))
        else:
            dinheiro -= aposta
            print ("Oh não! Você perdeu!
            print("Agora você tem um saldo de " + str(dinheiro))
    if tipo_de_aposta == "p":
        aposta_p = input("Escolha 'p' para um número par, ou 'i' para um número ímpar ")
        if aposta_p == "p":
            if num_random % 2 == 0:
                dinheiro += aposta
                print ("Parabéns você ganhou!")
                print("Agora você tem um saldo de " + str(dinheiro))
            else:
                dinheiro -= aposta
                print ("Oh não! Você perdeu!")
                print("Agora você tem um saldo de " + str(dinheiro))
        if aposta_p == "n":
            if num_random % 2 != 0:
                dinheiro += aposta
                print ("Parabéns você ganhou!")
                print("Agora você tem um saldo de " + str(dinheiro))
            else:
                dinheiro -= aposta
                print ("Oh não! Você perdeu!")
                print("Agora você tem um saldo de " + str(dinheiro))
