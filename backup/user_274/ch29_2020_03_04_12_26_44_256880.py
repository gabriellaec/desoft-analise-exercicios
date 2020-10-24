dep = float(input("Qual o depósito inicial?"))
tx = float(input("Qual a taxa de juros?"))

i = 1
total = dep

while i < 25:
    total = total*(1+tx)
	print("{0: .2f}".format(total))
    i=i+1
    
print("{0: .2f}".format(total-dep))
