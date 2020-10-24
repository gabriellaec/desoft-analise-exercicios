def valor_da_conta(valor):
    VAF=valor*1.1
    return VAF
valor = input('valor: ')
print('Valor da conta com 10%: R${0:.2f}'.format(valor_da_conta(valor)))