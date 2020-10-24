def lista_sufixos(string):
    contador=1
    tamanho=len(string)-1
    lista=[0]*tamanho
    while contador!=tamanho:
        letra=contador
        while letra<=tamanho:
            lista[contador]+=string[letra]
            letra+=1
        contador+=1
    return lista