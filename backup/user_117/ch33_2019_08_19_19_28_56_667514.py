i = 0
soma = 0
while i < 99:
    soma = soma + 1/2**i
    #soma = i * (1 - (1/2)**i) / 1 - 1/2
    i += 1    
print (soma)