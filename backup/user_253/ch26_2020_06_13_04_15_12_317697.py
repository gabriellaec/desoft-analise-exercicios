valor_casa = int(input('valor da casa?' ))
salario = int(input('sal?' ))
anos = int(input('tempo a ser pago' )
pm = valor_casa / anos / 12  
          
if pm < salario*30/100:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')
