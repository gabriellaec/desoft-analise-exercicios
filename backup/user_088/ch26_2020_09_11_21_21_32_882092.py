valor=float(input('valor da casa ?'))
salario=float(input('salario ?'))
anos=int(input('anos ?'))
 prestacao=(valor/12*anos)
    if(prestacao<=0.3*salario):
        print('Empréstimo aprovado')
    else:
        print ( 'Empréstimo não aprovado')