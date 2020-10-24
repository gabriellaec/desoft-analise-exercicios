def verifica_preco(titulo,dicionariocor,dicionariopreco):
    dicfinal={}
    for i in dicionariocor:
        for j in dicionariopreco:
            if dicionariocor.value(i)==dicionariocor.key(j):
                dicfinal[dicionariocor.key(i)]=dicionariopreco.value(j)
    for i in dicfinal:
        if i==titulo:
            return dicfinal.values(i)