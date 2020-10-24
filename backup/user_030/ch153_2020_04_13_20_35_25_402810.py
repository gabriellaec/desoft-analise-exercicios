def agrupa_por_idade(dicio):
    
    nomes = list(dicio.keys())
    
    idades = list(dicio.values())
    
    crianca = []
    
    adolescente = []
    
    adulto = []
    
    idoso = []
    
    for i in range(len(nomes)):
        
        if idades[i] <= 11:
            crianca.append(nomes[i])
            
        elif idades[i] <= 17:
            adolescente.append(nomes[i])
            
        elif idades[i] <= 59:
            adulto.append(nomes[i])
            
        else:
            idoso.append(nomes[i])
            
    faixas = {"Criança":crianca, "Adolescente":adolescente, "Adulto":adulto, "Idoso":idoso}
    return faixas