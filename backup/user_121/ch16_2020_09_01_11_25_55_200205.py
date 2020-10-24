valor_conta_restaurante = float(input('Qual foi o valor? '))
def calcula_conta(valor_conta_restaurante):
    valor_novo = valor_conta_restaurante * 1.10
    resultado = 'Valor da conta com 10%: R$ {:.2}'.format(valor_novo)
    return resultado