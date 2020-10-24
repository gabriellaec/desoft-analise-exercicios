def velocidade(v):
    x=(v-80)*5
    return x
a=float(input('Qual a velocidade? '))
b=velocidade(a)
if 80 >= a:
    print('Não foi multado')
else:
    print ('Valor da multa R$ ' + b)