c = float(input("valor da casa? ")
s = float(input("salário? ")
a = float(input("quantidade de anos? ")
p = c/(12*a)
          
if p>s*0.3:
	print('Empréstimo não aprovado')
else:
	print('Empréstimo aprovado')       
          