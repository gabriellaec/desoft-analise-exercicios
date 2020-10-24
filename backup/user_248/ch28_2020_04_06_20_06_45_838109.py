valores = []
for i in range(10):
    x[i]=1+1/2**i
    valores.append(x)
    
soma = 0.0
maior = valores[0]
for val in valores:
soma += val
if val > maior:
maior = val