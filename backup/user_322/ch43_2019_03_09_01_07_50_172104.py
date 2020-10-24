def numero_termos(n):
    contador = 1
    while n != 1:
        if n % 2 == 0:
            n = n/2
        elif n % 2 != 0:
            n = 3*n + 1
        contador += 1
    return contador
  
n = 1
tamanho = 0
while n < 1000000:
    if numero_termos(n) > tamanho:
        tamanho = numero_termos(n)
        x = n
    n = n + 1
    
print(x)    