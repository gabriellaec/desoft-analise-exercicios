def medias_por_inicial(dicionario):
    dic = {}
    for nome,nota in dicionario.items():
        i=1
        print(nome)
        inicial = nome[0]
        if inicial not in dic:
            dic[inicial] = nota
        else:
            i+=1
            dic[inicial] = (dic[inicial]+nota)/i
    return dic