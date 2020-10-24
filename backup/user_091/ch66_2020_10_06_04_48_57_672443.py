def lista_sufixos(nome):
    if nome=='':
        return []
    else:
        i=0
        lista=[nome]
        soma=''
        while i<len(nome)-1:
            soma=nome[i:]
            lista.append(soma)
            i+=1
        return lista
    
