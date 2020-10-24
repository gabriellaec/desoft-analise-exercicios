def ache_bigramas (str):
    lista=[]
    i=0
  
    while(i<len(str)-2):
        lista.append(str[i:i+2])
        i+=1
    return lista