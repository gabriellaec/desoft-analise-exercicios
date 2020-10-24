def agrupa_por_idade(dic_dados):
    nomes = list(dic_dados.keys())
    idades = list(dic_dados.values())
    crian = []
    adole = []
    adulto = []
    idoso= []
    for i in range(len(nomes)):
        if idades[i] <= 11:
            crian.append(nomes[i])
            
        elif idades[i] <= 17:
            adole.append(nomes[i])
            
        elif idades[i] <= 59:
            adulto.append(nomes[i])
            
        else:
            idoso.append(nomes[i])
            
    faixas={"criança":crian,"adolescente":adole,"adulto":adulto,"idoso":idoso}
    
    return faixas