vc = int(input('valor da casa?' )
s = int(input('salario?')
anos = int(input('tempo a ser pago')
meses = anos*12
pm = vc/meses            
if pm < s*30/100:
           print ('Empréstimo não aprovado')
else:
           print ('Empréstimo aprovado')
