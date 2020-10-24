soma = True
lista = [0]*100
n = 0
contador = 0
while soma: 
    if n < 100:
        lista [contador] = 1/(2**n)
        contador = contador + 1
        n=n+1
    else:
        break
print (sum(lista))
    
