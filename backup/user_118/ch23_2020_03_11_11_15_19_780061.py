def velocidade(c):
    x=(c-80)*5
    return x
v = input('Qual a velocidade?')
y=velocidade(v)
if y == 0:
    print('Não foi multado')
else:
    print ('Valor da multa R$ ' + v)