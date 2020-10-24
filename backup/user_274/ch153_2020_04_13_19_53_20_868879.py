def agrupa_por_idade(dicio):
    kid = []
    teen = []
    adult = []
    old = []
    for i,j in dicio.items():
        if j < 11:
            kid.append(i)
        elif j < 17:
            teen.append(i)
        elif j < 59:
            adult.append(i)
        else:
            old.append(i)
    
    dicio2 = {"criança" : kid, "adolescente" : teen, "adulto" : adult, "idoso" : old}
        
    return dicio2