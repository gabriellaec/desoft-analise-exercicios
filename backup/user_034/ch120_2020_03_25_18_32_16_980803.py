import random
dinheiro = 100
while dinheiro>0:
    print(dinheiro)
    a = int(input("Quanto deseja apostar?"))
    if a != 0:
        b = (input("Qual modo deseja jogar?"))
        if b == "n":
            numero = int(input("Qual numero deseja?"))
            numero_sortiado = random.randint(0,36)
            if numero == numero_sortiado:
                pagamento1 = a * 35 
                dinheiro = dinheiro + pagamento1
            else:
                dinheiro = dinheiro - a
        elif b == "p":
            numero_sortiado = random.randint(0,36)
            resto=numero_sortiado%2 == 0
            par_ou_impar = (input("par ou impar?"))
            if par_ou_impar == "p":
                if resto == True:
                	dinheiro = dinheiro + a
                else:
                    dinheiro = dinheiro - a
            if par_ou_impar == "i":
                if resto == False:
                	dinheiro = dinheiro + a
                else:
                    dinheiro = dinheiro - a
                    
    else:
        break