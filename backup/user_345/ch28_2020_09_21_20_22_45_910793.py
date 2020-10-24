soma =[0]*100
soma[0] = 1
i = 1
while soma < 100:
    soma[i] = soma[i-1] + 1/(2**i)
    soma = soma + 1
    
    print (soma)