soma = True
while soma:
    n = 0
    n=n+1
    if n < 100:
        lista = [1/(2**n)]*100
        soma_total = sum(lista)
    else:
        soma = False
print (soma_total)

    
