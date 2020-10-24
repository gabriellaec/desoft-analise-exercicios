valor_casa = int(input('valor da casa?' )
salario = float(input('salario?' )
anos = int(input('tempo a ser pago' )
meses = anos*12
pm = valor_casa/meses            
if pm < salario*30/100:
           print ('Empréstimo não aprovado')
else:
           print ('Empréstimo aprovado')
