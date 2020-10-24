def verifica_preco(titulo,dicionariocor,dicionariopreco):
    dicfinal={}
    for i,k in dicionariocor.items():
        for j,w in dicionariopreco.items():
            if k==j:
                dicfinal[i]=w
    for i in dicfinal:
        if i==titulo:
            return dicfinal[i]
