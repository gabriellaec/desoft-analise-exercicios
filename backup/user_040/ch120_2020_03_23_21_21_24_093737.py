from random import randint
dinheiros=100
while dinheiros>0:
    print (dinheiros)
    valor = int(input("valor: "))
    if valor == 0:
        dinheiros=0
    else:
        aleatório = randint(0,36)
        aposta = input("n ou p: ")
        if aposta == "n":
            número = int(input("número: "))
            if (número==aleatório):
                dinheiro += valor*35
            else:
                dinheiro -= valor                    
        elif aposta == "p":
            par_ou_impar = int(inpu("p ou i: "))
            if par_ou_impar == "p":
                if aleatório%2 == 0:
                    dinheiros+=valor
                else:
                    dinheiros-=valor
            elif par_ou_impar == "i":
                if aleatório%2 != 0:
                    dinheiros+=valor
                elif aleatório%2 == 0 and dinheiros == valor:
                    dinheiros=0
                else:
                    dinheiros -= valor