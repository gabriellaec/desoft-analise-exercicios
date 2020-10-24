def responde_valor_da_conta(valor):
    valor = valor * 1.10
    print(f'Valor da conta com 10%:{valor}')

valor = float(input('Qual o valor da conta: '))
responde_valor_da_conta(valor)
