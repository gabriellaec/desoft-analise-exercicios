def soma_lista(lista):
    i=0
    numero_de_elementos=len(lista)
    soma=0
    while i<numero_de_elementos:
        soma+=lista[i]
        i+=1
    return soma   
print(soma_lista(lista))