def agrupa_por_idade(dicio):
    kid = []
    teen = []
    adult = []
    old = []
    for i,j in dicio.items():
        if j < 11:
            kid.append(i)
        if j < 17:
            teen.append(i)
        if j < 59:
            adult.append(i)
        else:
            old.append(i)
    ages = [kid, teen, adult, old]
    faixa = ["criança", "adolescente", "adulto", "idoso"]
    dicio2 = {}
    for i in 4:
        dicio2[faixa[i]]={ages[i]}
        
    return dicio2