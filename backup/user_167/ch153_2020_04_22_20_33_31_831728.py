def agrupa_por_idade (dic):
    nv={}
    for k,v in dic. items():
        if v <= 11:
            nv["crianca"]=k
        if v >=12 and v <=17:
            nv["adolecente"]=k
        if v>=18 and v <59:
            nv["adulto"]=k
        if v>=60:
            nv["idoso"]=k
    return nv  
 