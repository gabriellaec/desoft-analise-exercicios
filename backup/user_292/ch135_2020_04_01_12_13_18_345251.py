def equaliza_imagem(listaP):
    listaE=[]
    a=len(listaP)
    x=0
    while x<=a-1:
        listaP[x]=listaP[x]*k
        if listaP[x]>255:
            listaP[x]==255
            x+=1
            listaE.append(listaP[x])
        else:
            x+=1
            listaE.append(listaP[x])
    return listaE
            
    
    
    