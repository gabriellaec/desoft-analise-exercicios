velocidade = int(input('Qual a velocidade do carro em km/h ? '))
def multa_de_velocidade(velocidade):
    if velocidade<=80:
        print('Não foi multado')
    else:
        velocidade_extra = velocidade - 80
        multa = velocidade_extra*5
        print('Multa de R${0:.2f}'.format(multa))
    return 'a'
multa_de_velocidade(velocidade)