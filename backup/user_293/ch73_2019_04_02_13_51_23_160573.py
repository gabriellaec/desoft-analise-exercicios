def remove_vogais(string):
    lista=lista(string)
    i=0
    lista_final=[]
    while i < len(lista):
        if lista[i] == "aeiou":
            del(lista[i])
        else:
            i+=1
    lista_final = ".join(lista)"
    return lista_final

        
