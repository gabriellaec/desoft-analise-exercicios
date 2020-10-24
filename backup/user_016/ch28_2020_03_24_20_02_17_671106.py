soma = True
n = 0
contador = 0
while soma:
    if n < 100:
        lista = [1/(2**n)]*100
        print (lista[contador])
        contador = contador + 1
        n=n+1
    else:
        soma = False
soma_total = sum(lista)
print (soma_total)

    
