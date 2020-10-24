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
        if letra not in cont:
            cont[letra] = 1
        else:
            cont[letra] += 1
    for k,v in alunos.items():
        c = 0
        letra = 'n'
        for i in k:
            if c == 0:
                letra = i
            c += 1
        if letra not in dic:
            dic[letra] = v
        else:
            dic[letra] += v
    print(dic)
    for i in dic:
        if dic[i] > 1:
            dic[i] = dic[i]/cont[i]
    
    print(cont)
    return dic
        
           
            