def conta_termos(n):
    contador = 1
    while n!=1:
        if n%2 == 0:
            n = n/2
            contador += 1
        elif n%2 != 0:
            n = 3*n+1
            contador += 1
    return contador

n = [2]*999
i=0
while i < len(n)-1:
    n[i+1]=n[i]+1
    i += 1

maxdocontador = 1
numerorespons = 0

for numero in n:
    cont = conta_termos(numero)
    if cont > maxdocontador:
        maxdocontador = cont
        numerorespons = numero

print(numerorespons)
    
        
    