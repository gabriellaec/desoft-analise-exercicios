
      def inverte_dicionario(dic):
    listanomes=[]
    listaidades=[]
    dicinvertido={}
    for chave in dic.keys():
        listanomes.append(chave)
    for valor in dic.values():
        listaidades.append(valor)
    
    for i in range(len(listanomes)):
        dicinvertido[listaidades[i]]=listanomes[i]
    
    for chave,valor in dicinvertido.items():
        for chave2,valor2 in dicinvertido.items():
            if chave==chave2:
                listachave=[]
                listachave.append(valor + valor2)
        
    return dicinvertido  