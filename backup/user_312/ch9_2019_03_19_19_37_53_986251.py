def lista_sufixos(string):
    lista=[]
    if len(string)==1:
        return lista
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