exp = 0
soma = 1
while exp < 100:
    soma = 1/2**exp
    soma += soma
    exp += 1
    
print (soma)
