velocidade=float(input('Qual a velocidade do seu carro em km/h? :'))
if velocidade > 80:
    print('Você foi multado')
    print('Você terá que pagar uma multa de {:.2f} reais'.format((velocidade-80)*5))
else:
    print('Não foi multado')