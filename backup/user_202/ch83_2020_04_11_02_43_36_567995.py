def medias_por_inicial(alunos):
    dic = {}
    cont = {}
    for k,v in alunos.items():
        c = 0
        letra = 'n'
        for i in k:
            if c == 0:
                letra = i
            c += 1
        cont[k] += 1
    for k,v in alunos.items():
        c = 0
        letra = 'n'
        for i in k:
            if c == 0:
                letra = i
            c += 1
        dic[k] += v
    for i in dic:
        if dic[i] > 1:
            dic[i] = dic[i]/cont[i]
    return dic
        
           
            