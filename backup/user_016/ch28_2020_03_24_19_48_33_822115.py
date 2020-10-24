soma = True
contador = 0
while soma:
    lista = [1/(2**n)]*100
    n = 0
    n=n+1
    if n < 100:
        soma_total = sum(lista)
        contador = contador + 1
    else:
        soma = False
print (soma_total)

    
