from random import randint
dinheiros=100
while (dinheiros>0):
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
                dinheiros += valor*35
            else:
                dinheiros -= valor                    
        elif aposta == "p":
            par_ou_impar = int(input("p ou im: "))
            if par_ou_impar == "p":
                if aleatório%2 == 0:
                    dinheiros+=valor
                else:
                    dinheiros-=valor
            elif par_ou_impar == "im":
                if aleatório%2 != 0:
                    dinheiros+=valor
                elif aleatório%2 == 0 and dinheiros == valor:
                    dinheiros=0
                else:
                    dinheiros -= valor