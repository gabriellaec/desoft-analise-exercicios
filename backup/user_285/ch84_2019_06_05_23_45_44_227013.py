def inverte_dicionario(dic):
    listanomes=[]
    listaidades=[]
    dicinvertido={}
    for chave in dic.keys():
        listanomes.append(chave)
    for valor in dic.values():
        listaidades.append(valor)
        
    for i in range(len(listaidades)):
        for e in range(len(listaidades)):
            if listaidades[i]==listaidades[e] and i!=e:
                listachaves=[]
                listavalores=[]
                listachaves.append(listaidades[i])
                listavalores.append(listanomes[i]+listanomes[e])
    for i in range(len(listachaves)):
        dicinvertido[listachaves[i]]=listavalores[i]
        
    return dicinvertido  