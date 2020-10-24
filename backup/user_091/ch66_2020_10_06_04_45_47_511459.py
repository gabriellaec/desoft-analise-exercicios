def lista_sufixos(nome):
    if nome=='':
        return []
    else:
        i=0
        lista=[nome]
        soma=''
        while i<len(nome):
            del nome[i]
            lista.append(nome)
            i+=1
        
    return lista
    
    
