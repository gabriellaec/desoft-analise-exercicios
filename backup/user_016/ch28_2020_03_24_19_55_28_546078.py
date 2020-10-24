soma = True
n = -1
while soma:
    n=n+1
    if n < 100:
        lista = [1/(2**n)]*100 
    else:
        soma = False
soma_total = sum(lista)
print (soma_total)

    
