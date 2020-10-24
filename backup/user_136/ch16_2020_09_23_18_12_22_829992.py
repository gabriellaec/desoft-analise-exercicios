def valor_da_conta (p):
    valor= (p*0.1) + p
    return "Valor da conta com 10%: R$ {0:.2f}".format(valor)

w= int(input('qual o valor da conta? '))
print (valor_da_conta(w))