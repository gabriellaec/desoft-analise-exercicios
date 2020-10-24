def agrupa_por_idade(dic):
    novodic={}
    #elif v>=12 and v<=17:
    novodic.setdefault('adolescente',[])
    for k,v in dic.items():
        if v <=11:
            novodic.setdefault('criança',[]).append(k)
        elif v>=18 and v<=59:
             novodic.setdefault('adulto',[]).append(k)
        else:
             novodic.setdefault('idoso',[]).append(k)

    return novodic
       