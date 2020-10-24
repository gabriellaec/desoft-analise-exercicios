print('Qual o valor da conta?')
valor_da_conta = float(input())

def valor_a_pagar(valor_inicial):
    y = valor_inicial*0.9
    return y

valor_com_desconto = valor_a_pagar(valor_da_conta)
print("Valor da conta com 10%: R$ {0:.2f}".format(valor_com_desconto))