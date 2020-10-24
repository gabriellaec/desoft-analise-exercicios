km = int(input('Qual a velocidade do carro? '))
if km >80:
    multado = (km-80)*5
    print('A multa é de R$: {0:.2f}'.format(multado))
elif km <= 80:
    print('Não foi multado.')