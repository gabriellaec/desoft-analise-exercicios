c = int(input("valor da casa? ")
s = int(input("salário? ")
a = int(input("quantidade de anos? ")
p = c/(12*a)
          
if p>s*0.30:
	print('Empréstimo não aprovado')
else:
	print('Empréstimo aprovado')        
          
          