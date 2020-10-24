v = float(input('Qual a velocidade do seu carro?'))
def(v):
    if v>80:
        return 'Você foi multado!'
        a = v - 80
        m = 5*a
        return 'O preço da multa é {0:.2f} reais!'.format(m)
    else:
        return 'Não foi multado'
    
    