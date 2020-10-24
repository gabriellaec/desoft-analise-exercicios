def soma10per(preco):
    return preco*1.1

preco = float(input("Escreva o valor da conta: "))
print("Valor da conta com 10%: R$ {0:.2f}".format(soma10per(preco)))
