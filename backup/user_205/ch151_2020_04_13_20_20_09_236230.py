def classifica_lista(lista):
    if len(lista)<2:
        return "nenhum"
    crescente = lista[0]
    descrescente = lista[0]           #Definindo começo pra percorrer
    for numeros in range(len(lista)-1):
        if lista[numeros+1] > crescente:
            #Se o proximo for maior q o inicio
            crescente = lista[numeros+1] 
        else: 
            decrescente = lista[numeros+1]
    
            
    