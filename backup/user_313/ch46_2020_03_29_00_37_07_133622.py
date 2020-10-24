y = True
c = 0

resultado =[]
def numero_no_indice(lista):
    c = len(lista)
    contador = 0
    while contador != c:
        if lista[contador] == contador:
            b = lista[contador]
            resultado.append(b)
            contador += 1
        else:
            contador +=1
    #del resultado[0]
    return(resultado)

