velocidade = int(input('Qual a velocidade do carro em km/h? '))
def f(x):
    if x > 80:
        multa = (x - 80) * 5.00
        resultado = print('Você foi multado em R$ {:.2f}'.format(multa))
    else:
        resultado = print('Não foi multado')
    return resultado

f(velocidade)