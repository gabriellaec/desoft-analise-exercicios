valor = float(input('Quanto custa a casa?'))
salario = float(input('Qual seu salário?'))
anos = float(input('Quantos anos?'))
meses = anos*12
prestação = valor / meses
if prestação > 0.3*salario:
    print ("Empréstimo não aprovado")
else:
    print("'Empréstimo aprovado'")