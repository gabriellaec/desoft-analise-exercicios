def aniversariantes_de_setembro(dicio):
    setembro = {}
    nomes = []
    datas = []
    for n,d in dicio.items():
        nomes.append(n)
        datas.append(d)
    i=0
    while i <len(datas):
        if datas[i][3:5]=="09":
            setembro[nomes[i]] = datas[i]
        i+=1
    return setembro