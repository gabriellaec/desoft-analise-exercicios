def agrupa_por_idade(f):
    f={}
    lf={}
    for c,v in f.items():
        if v<=11:
            lf[criança]=c
        elif 12<=v<=17:
            lf[adolescente]=c
        elif 18<=v<=59:
            lf[adulto]=c
        else:
            lf[idoso]=c
    return(lf)
        