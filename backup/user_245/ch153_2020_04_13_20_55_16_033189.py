def classifica_lista(dicio):
    classifica = {}
'''
faixa etaria:
crianca anos<=11
adolescente 12<=anos<=17
adulto 18<=anos<=59
idoso 60<=anos 
'''
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