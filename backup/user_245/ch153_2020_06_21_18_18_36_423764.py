def classifica_lista(dicio):
    classifica = {}
    for i in dicio:
        if dicio.keys(i)<=11:
            classifica["criança"] = dicio.values(i)
        if 12<=dicio.keys(i)<=17:
            classifica["adolescente"] = dicio.values(i)
        if 18<=dicio.keys(i)<=59:
            classifica["adulto"] = dicio.values(i)
        if 60<=dicio.keys(i):
            classifica["idoso"] = dicio.values(i)
    return classifica