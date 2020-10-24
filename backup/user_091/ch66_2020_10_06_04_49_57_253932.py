def lista_sufixos(nome):
    if nome=='':
        return []
    else:
        i=1
        lista=[nome]
        soma=''
        while i<len(nome):
            soma=nome[i:]
            lista.append(soma)
            i+=1
        return lista
    
