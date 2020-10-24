c=float(input("Qual a velocidade do carro?"))

if c<=80: 
    print('Não foi multado')
else: 
    z=(c-80)*5
    print("Você foi multado. A multa é de {0:.2f}".format(z))