vc = float(input('valor casas?')
salario=float(input('salario')
anos= int(input('anos')
prestação= vc/anos/12
if prestação > salario*30/100:
    print ('Empréstimo não aprovado')
else:
    ('Empréstimo aprovado')