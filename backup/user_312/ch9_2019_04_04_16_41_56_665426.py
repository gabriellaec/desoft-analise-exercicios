def lista_sufixos(string):
    lista=[]
    if len(string)==1:
        lista.append(string)
        return lista
    contador=1
    tamanho=len(string)-1
    while contador<=tamanho:
        lista.append(string[contador:tamanho])
        contador+=1
    return lista