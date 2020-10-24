casa = float(input('valor da casa:'))
salario = float(input('salario:'))
anos = float(input('quantos anor:'))
if casa/12*anos >= 0.3 * salario:
     print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')