numero = 1
n = 2
termos = 1
maximo = 0
x = 0
while n < 1000:
    x = n - 1    
    termos = 1
    while n != 1:
        termos += 1
        if n % 2 == 0:
           n = n/2
        
        else:
           n = 3*n + 1
        
    if maximo < termos:
        maximo = termos
        numero = x + 1
   
    n = x + 2 

print (numero)