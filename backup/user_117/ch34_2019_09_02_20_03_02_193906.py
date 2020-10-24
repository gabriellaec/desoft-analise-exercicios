d = float(input("Depósito inicial: "))
j = float(input("Taxa de juros: "))
          
s = d
i+=0
          
while i < 24:
	print ("{0:2d} {1:.2f}".format(i,s))
    s = s * (1 + j /100)
    i += 1
print ("{0:2d} {1:.2f}".format(i,s))
          