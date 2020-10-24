def medias_por_inicial(dicionario):
    novo={}
    listanotas=[]
    listanomes=[]
    for e in dicionario.values():
        listanotas.append(e)
    for e in dicionario:
        listanomes.append(e)
    c=0
    while c<len(listanotas):
        a=1
        soma=listanotas[c]
        novo[listanomes[c][0]]=soma
        p=1
        while p<len(listanotas):
            if listanomes[c][0]==listanomes[p][0]:
                a+=1
                soma=(soma+listanotas[p])/a
                novo[listanomes[c][0]]=soma
                del(listanomes[p])
                del(listanotas[p])
                p+=1
            else:
                p+=1
        c+=1
    return novo