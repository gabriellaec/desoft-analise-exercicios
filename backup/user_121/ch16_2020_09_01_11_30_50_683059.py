pergunta = float(input('Digite aqui o valor da conta: '))
def calcula(x):
    valor_novo = x * 1.10
    resultado = 'Valor da conta com 10%: R$ {:.2}'.format(valor_novo)
    return resultado
calcula(pergunta)