def aniversariantes_de_setembro(dictio):
    aniv_set=dict()
    nomes=[]
    datas=[]
    for k,v in dictio.items():
        nomes.append(k)
        datas.append(v)
    for h in range(0,len(datas)):
        if datas[h][3:5]=="09":
            aniv_set[nomes[h]]=datas[h]
    return aniv_set