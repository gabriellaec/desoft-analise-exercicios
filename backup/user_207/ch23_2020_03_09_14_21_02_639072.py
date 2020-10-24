velocidade_carro = int(input ('Qual era a velocidade do veículo, em Km/H (formato XYZ) '))

def multa (velocidade_carro):
    y = 5 * (velocidade_carro - 80)
    return y

if velocidade_carro > 80:
    print ("Você foi multado em {0:.2f} reais" .format(multa(velocidade_carro)))
else:
    print ('Não foi multado')
