def f(v):
    if v>80:
        a = v - 80
        m = 5*a
        return 'Você foi multado! O preço da multa é {0:.2f} reais!'.format(m)
    else:
        return 'Não foi multado'
    
t = float(input('Qual a velocidade do seu carro?'))