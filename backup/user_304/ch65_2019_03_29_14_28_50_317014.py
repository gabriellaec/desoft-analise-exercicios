def acha_bigramas (palavra):
    lista=[]
    i=0
    while i<(len(palavra)-1):
        bigrama= palavra[i]+palavra[i+1]
        lista.append(bigrama)
        i=i+1
        x=0
        y=1
        if bigrama[x]==bigrama[x+y]:
            del bigrama[x+y]
            x=x+1
            y=y+1
        return bigrama
            
        