def agrupa_por_idade(dicionario):
    nomes=list(dicionario.keys())
    idades=list(dicionario.values())
    cri=[]
    ado=[]
    adu=[]
    ido=[]
    for i in range(len(nomes)):
        if idades[i]<=11:
            cri.append(nomes[i])
        elif idades[i]<=17:
            ado.append(nomes[i])
        elif idades[i]<=59:
            adu.append(nomes[i])
        else:
            ido.append(nomes[i])
            
    faixa_etarias={"criança":cri,"adolescente":ado,"adulto":adu,"idoso":ido}
    return faixas_etarias