def interseccao_chaves(d1,d2):
    listeras=[]
    for nome,idade in d1.items():
        for nomeras,idads in d2.items():
            if nome==nomeras and nome not in listeras:
                listeras.append(nome)
    return listeras