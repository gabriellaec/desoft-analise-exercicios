valor = float(input('Qual é o valor da conta?'))
def calcula_valor(valor):
    valor_novo = valor + (valor/10)
    decimal = round(valor_novo, 2)
    frase = 'Valor da conta com 10%: R$ {}'.format(decimal)
    return frase
print(calcula_valor(valor))