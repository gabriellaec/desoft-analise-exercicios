dep0=float(input('Qual o seu depósito inicial? '))
depm=float(input('Qual o seu depósito mensal? '))
txj=float(input('Qual a txa de juros? '))

i=2

while i<=24:
	m=dep0*((1+txj)**i)+(depm*i)*((1+txj/100)**(i-1))
	print (('{0:.2f}').format(m))
	i+=1
h=m-dep0-(depm*24)
print (('{0:.2f}').format(h))


