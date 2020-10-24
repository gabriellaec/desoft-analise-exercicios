a = int(input('Valor da casa: '))
b = int(input('Salário: '))
c = int(input('Anos a pagar: '))
if b > (a/(c*12))/0.3:
	print ('Empréstimo aprovado')
else:    
    print ('Empréstimo não aprovado')