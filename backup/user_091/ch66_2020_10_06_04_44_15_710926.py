def lista_sufixos(nome):
    i=0
    lista=[nome]
    soma=''
    while i<len(nome):
        soma-=nome[i]
        lista.append(soma)
        i+=1
        
    return lista
    
    
