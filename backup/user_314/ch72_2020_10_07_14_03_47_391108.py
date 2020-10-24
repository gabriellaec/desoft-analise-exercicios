def lista_caracteres (str):
    
    lista_c=[]
    i=0

    while(i<len(str)):
        x=str[i]

        if not x in lista_c:
            lista_c.append(x)

        i+=1

    return lista_c
