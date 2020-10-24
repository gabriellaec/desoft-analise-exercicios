def classifica_lista(l):
    if len(lista_numeros)<2:
        return "nenhum"
    i=lista_numeros[1]-lista_numeros[0]
  
    if i>0:
        for i in range (len(lista_numeros)-1):
            if lista_numeros[i+1]-lista_numeros[i]<=0:
                return "nenhum"
    if i<0:
         for i in range (len(lista_numeros)-1):
            if lista_numeros[i+1]-lista_numeros[i]>=0:
                return "nenhum"
            
    if l==0:
        return "nenhum"
    elif l>0:
        return "crescente"
    elif l<0:
        return "decrescente"
    