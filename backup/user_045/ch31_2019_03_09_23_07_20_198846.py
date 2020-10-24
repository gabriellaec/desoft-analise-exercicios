valorcasa=int(input('valor da casa?'))
salario=int(input('salario?'))
anos=int(input('anos pagando?'))
if valorcasa/(12*anos)<=salario*0.3:
    return 'Empréstimo aprovado'
else:
    return 'Empréstimo não aprovado'
