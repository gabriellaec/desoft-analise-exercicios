def lista_de_string (str):
    lista=[]
    i=0

    while(i<len(str)-1):
        lista.append(str[i:])
        i+=1
  
    return lista
