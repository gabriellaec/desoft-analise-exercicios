def remove_vogais(string):
    lista=list(string)
    i=0
    while i < len(lista):
        if lista[i] in "aeiou":
            del lista[i]
        else:
            i+=1
    lista_final = "".join(lista)
    return lista_final

        
