def agrupa_por_idade (dic):
    nv={}
    for k,v in dic. items():
        if v <= 11:
            nv[k]="crianca"
        if v >=12 and v <=17:
            nv[k]="adolecente"
        if v>=18 and v <59:
            nv[k]="adulto"
        if v>=60:
            nv[k]="idoso"
    return nv  
 