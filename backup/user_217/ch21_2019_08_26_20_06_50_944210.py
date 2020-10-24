def valor_da_conta(valor):
    com10 = valor + valor*(10/100) 
    return com10

valor = float(input('Qual valor da conta?:' ))
print("Valor da conta com 10%: R${0:.2f}".format(valor_da_conta(valor)))