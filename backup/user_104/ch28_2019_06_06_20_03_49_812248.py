velocidade = int(input('Qual é a velocidade do carro?'))
def multa(velocidade):
    if velocidade > 80:
        valor = (velocidade-80)*5
        decimal = '%.2f' % valor
        x = 'Você foi multado em R${} !'.format(decimal)
    else:
        x ='Não foi multado'
    return x
print(multa(velocidade))