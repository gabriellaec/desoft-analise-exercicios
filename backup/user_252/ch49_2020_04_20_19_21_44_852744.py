def inverte_lista(lista):
    listai=[]
    a=len(lista)
    i=0
    while i < len(lista):
        n=lista[a-i]
        listai.append(n)
        i+=1
    return listai
        
        