def remove_vogais(string):
    lista=list(string)
    contador=0
    lista_final=[]
    for i in lista:
        if i=='a' or i=='e' or i=='o' or i=='i' or i=='u':
            del(lista[contador])
        contador+=1
    '''for i in lista:
        lista_final+=i'''
    lista_final=''.join(lista)
    return lista_final