def lista_sufixos(string):
    if len(string)==1:
        return []
    contador=1
    tamanho=len(string)-1
    lista=[0]*tamanho
    while contador<=tamanho:
        letra=contador
        while letra<=tamanho:
            if string[letra]!=" ":
            	lista[contador]+=string[letra]
            letra+=1
        contador+=1
    return lista