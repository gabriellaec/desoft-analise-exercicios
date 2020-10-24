#***** O BRABO PRA DAR APPEND EM DIC*******
'''def agrupa_por_idade(dic):
    novodic={}
    for k,v in dic.items():
        if v <=11:
            novodic.setdefault('crianca',[]).append(k)
        elif v>=12 and v<=17:
             novodic.setdefault('adolescente',[]).append(k)
        elif v>=18 and v<=59:
             novodic.setdefault('adulto',[]).append(k)
        else:
             novodic.setdefault('idoso',[]).append(k)

    return novodic '''
def agrupa_por_idade(dic):
    novodic={'criança':[],'adolescente':[],'adulto':[],'idoso':[]}
    for k,v in dic.items():
        if v <=11:
            novodic['criança'].append(k)
        elif v>=12 and v<=17:
             novodic['adolescente'].append(k)
        elif v>=18 and v<=59:
             novodic['adulto'].append(k)
        else:
             novodic['idoso'].append(k)
    return novodic
    