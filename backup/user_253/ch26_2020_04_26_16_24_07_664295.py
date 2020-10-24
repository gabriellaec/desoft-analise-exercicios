vc = float(input('valor casas?')
sal = int(input('quanto vc ganha?'))
anos= int(input('anos')
prestação= vc/anos/12
if prestação > sal*30/100:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')