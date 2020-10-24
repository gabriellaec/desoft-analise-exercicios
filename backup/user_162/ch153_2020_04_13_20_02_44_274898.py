def agrupa_por_idade(n_idade):
    agrupa = {}
    agrupa["criança"] = []
    agrupa["adolescente"] = []
    agrupa["adulto"] = []
    agrupa["idoso"] = []
    for n, i in n_idade.items():
        if i < 12:
            i = "criança"
        elif 12 <= i < 18:
            i = "adolescente"
        elif 18 <= i < 60:
            i = "adulto"
        else:
            i = "idoso"
        if i not in agrupa:
            agrupa[i] = []
        agrupa[i].append(n)
    return agrupa
    
