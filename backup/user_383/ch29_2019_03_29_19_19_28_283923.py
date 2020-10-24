def calcula_aumento(preco):
    if preco>1250:
        print(preco + preco*0.1)
    elif preco<=1250:
        print(preco + preco*0.15)
    return preco
 