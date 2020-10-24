dinheiro = 100

while dinheiro > 0:
    print ("Você possui {} dinheiros".format(dinheiro))
    aposta = int ( input ("Qual valor você deseja apostar? ") )
    if aposta == 0:
        break
    else:
        par_ou_impar = input ("A aposta é um número par ou ímpar? ")
        if par_ou_impar == "n":
            número = random.randint(1,36)
            chute = int(("Qual você acha que foi o número de 1 a 36? "))
            if chuta == número:
                dinheiro += 35*aposta
        if par_ou_impar == "p":
            p_ou_i = input ('Escolha par "p" ou ímpar "i"' )
            
            