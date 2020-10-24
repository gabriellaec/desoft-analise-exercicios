a=int(input('Qual a velocidade do carro? '))
def multa(a):
    y=(a-80)*5
    if a<=80:
        return 'Não foi multado'
    else:
        return 'Voce foi multado em R$ {0:.2f}'.format(y)

