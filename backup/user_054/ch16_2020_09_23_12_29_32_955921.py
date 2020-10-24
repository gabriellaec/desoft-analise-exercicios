conta = float (input ('Valor da conta: R$  '))
def conta_com_10_di_disconto (conta):
    conta += conta*10/100
    return conta
print ('Valor da conta com 10%: R$ {0:.2f}'.format(conta))