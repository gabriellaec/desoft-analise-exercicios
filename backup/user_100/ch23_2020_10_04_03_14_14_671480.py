def f(v):
    if v>80:
        a = v - 80
        m = 5*a
        print('Você foi multado! O preço da multa é {0:.2f} reais!'.format(m))
    else:
        print('Não foi multado')
    
t = float(input('Qual a velocidade do seu carro?'))
print(f(t))
