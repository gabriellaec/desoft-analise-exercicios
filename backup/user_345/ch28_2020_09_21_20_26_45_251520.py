soma = [0.0]*100
soma[0] = 1.0
i = 1.0
while i < 100:
    soma[i] = soma[i-1] + 1/(2**i)
    soma = soma + 1.0
    
    print (soma)