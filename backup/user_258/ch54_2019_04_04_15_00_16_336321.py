def junta_nome_sobrenome(nomes,sobrenomes):
    string=[]
    i=0
    while i<len(nomes):
        string.append(nomes[i]+' '+sobrenomes[i])
        i+=1
    return string