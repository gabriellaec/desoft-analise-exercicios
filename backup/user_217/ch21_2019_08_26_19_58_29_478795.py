def valor_da_conta(valor):
    valor = int(input('Qual valor da conta?:' ))
    com10% = valor + valor*(10/100) 
    return com10%
print("Valor da conta com 10%: R${0}".format(com10%))