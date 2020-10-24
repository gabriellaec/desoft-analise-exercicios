def interseccao_valores(d1,d2):
    listeras=[]
    for nome,idade in d1.items():
        for nomeras,idads in d2.items():
            if idade==idads and idade not in listeras:
                listeras.append(idade)
    return listeras