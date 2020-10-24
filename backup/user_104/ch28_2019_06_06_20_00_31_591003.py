velocidade = input('Qual é a velocidade do carro?')
def multa(velocidade):
    if velocidade > 80:
        valor = (velocidade-80)*5
        x = 'Você foi multado em R${} !'.format(valor)
    else:
        x ='Não foi multado'
    return x
print(multa(velocidade))