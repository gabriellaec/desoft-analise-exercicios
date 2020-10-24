def acha_bigramas(pal):
    contador1=0
    contador2=1
    listabigramas=[]
    palavra=[]
    for i in pal:
        palavra.append(i)
        
    while contador1<len(pal)-1:
        listabigramas.append(palavra[contador1]+palavra[contador2])
        contador1+=1
        contador2+=1
                
    return listabigramas
