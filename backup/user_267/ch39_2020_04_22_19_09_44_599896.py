
def seq(n):
    termos = 1
    if n < 1000:
        while n != 1:
            if n % 2 == 0:
                n = n/2
                termos += 1
            else:
                n = 3*n + 1
                termos += 1
    return termos
maior = 0
inicio = 0
for a in range(1,1000):
    termos2 = seq(a)
    if termos2 > maior:
        maior = termos2
        inicio = a
print(a)
   
            
            