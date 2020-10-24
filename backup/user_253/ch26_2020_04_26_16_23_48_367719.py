vc = float(input('valor casas?')
salario = int(input('quanto vc ganha?'))
anos= int(input('anos')
prestação= vc/anos/12
if prestação > salario*30/100:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')