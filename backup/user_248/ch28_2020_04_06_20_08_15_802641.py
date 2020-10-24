valores = []
for i in range(100):
    x=1+1/2**i
    valores.append(x)
    
soma = 0.0
maior = valores[0]
for val in valores:
    soma += val
    if val > maior:
        maior = val
print("Soma = {0}, maior valor = {1}".format(soma, maior))