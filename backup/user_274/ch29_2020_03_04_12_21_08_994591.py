dep = float(input("Qual o depósito inicial?"))
tx = float(input("Qual a taxa de juros?"))

i = 1
total = dep

while i < 25:
    total = total*(1+tx)
	print("Mês {0}: R$ {1: .2f}".format(i,total))
    i=i+1
    
print("R$ {0: .2f}".format(total-dep))
