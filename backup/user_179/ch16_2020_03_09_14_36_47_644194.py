valor_da_conta = input('Quanto deu a conta? ')
def total (valor_da_conta):
    valor_total = valor_da_conta**1.1
    return valor_total
total (10)
print ('Valor da conta com 10%: R$ ' + valor_total)