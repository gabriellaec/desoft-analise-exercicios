soma = True
n = 0
lista = [1/(2**n)]*100
contador = 0
while soma:
    if n < 100:
        contador = contador + 1
        n=n+1
    else:
        soma = False
soma_total = sum(lista)
print (soma_total)

    
