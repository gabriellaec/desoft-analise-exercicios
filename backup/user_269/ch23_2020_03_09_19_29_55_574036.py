a=int(input("Qual a sua velocidade "))
b=(a-80)*5
if a <= 80:
    print('Não foi multado')
else:
    print(O valor da multa e {0:.2f}.format(b))