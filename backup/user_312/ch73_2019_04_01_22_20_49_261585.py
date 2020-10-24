def remove_vogais(string):
    lista=list(string)
    contador=0
    lista_final=[]
    while contador<len(lista):
        if lista[contador]=='a' or lista[contador]=='e' or lista[contador]=='o' or lista[contador]=='i' or lista[contador]=='u':
            del(lista[contador])
        else:
            contador+=1
    lista_final=''.join(lista)
    return lista_final

print(remove_vogais("banana"))