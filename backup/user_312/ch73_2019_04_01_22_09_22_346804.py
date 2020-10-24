def remove_vogais(string):
    lista=list(string)
    lista_final=[]
    for i in lista:
        if lista[i]=='a' or lista[i]=='e' or lista[i]=='o' or lista[i]=='i' or lista[i]=='u':
            del(lista[i])
    for i in lista:
        lista_final+=lista[i]
    return lista_final