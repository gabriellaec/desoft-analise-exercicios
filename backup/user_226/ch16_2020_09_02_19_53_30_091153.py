def responde_valor_da_conta(valor):
    valor = valor * 1.10
    print('Valor da cont com 10%:{0}').format(valor)

valor = float(input('Qual o valor da conta: '))
responde_valor_da_conta(valor)