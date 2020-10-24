exp = 0
soma = 1
while exp < 100:
    soma = 1/2**exp
    exp += 1
    soma += soma
    
print (soma)
