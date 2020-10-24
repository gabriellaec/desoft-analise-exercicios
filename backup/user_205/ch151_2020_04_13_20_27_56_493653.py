def classifica_lista(lista):
    if len(lista)<2:
        return "nenhum"
    crescente = lista[0]
    decrescente = lista[0]
    a=0#Definindo começo pra percorrer
    for numeros in range(len(lista)-1):
        while a!= 1:
            if lista[numeros+1] > crescente:
            #Se o proximo for maior q o inicio
                crescente = lista[numeros+1] 
            else: 
                decrescente = lista[numeros+1]
            a=1
    #Se o ultimo elemento da lista for igual ao crescente, é crescente
    ultimo_elemento = lista[-1]
    if crescente == ultimo_elemento:
        return "crescente"
    elif len(lista)<2:
        return "nenhum"
    elif decrescente == ultimo_elemento:
        return "decrescente"
    else:
        return "nenhum"
    
            
    