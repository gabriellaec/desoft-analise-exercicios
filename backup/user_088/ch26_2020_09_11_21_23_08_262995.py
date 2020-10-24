valor=float(input('valor da casa ?'))
salario=float(input('salario ?'))
anos=int(input('anos ?'))
meses =12*anos
prestacao=(valor/meses)
    if(prestacao>0.3*salario):
        print('Empréstimo não aprovado')
    else:
        print ( 'Empréstimo aprovado')