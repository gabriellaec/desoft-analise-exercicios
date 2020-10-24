def agrupa_por_idade (nomes_idades):
    faixas_etarias = {'criança':[], 'adolescente': [], 'adulto': [], 'idoso': []}
    
    for k, v in nomes_idades.items():
        if v<=11:
            faixas_etarias['criança'].append(k)
        
        elif v<=17:
            faixas_etarias['adolescente'].append(k)
        
        elif v<=59:
            faixas_etarias['adulto'].append(k)
        
        else:
            faixas_etarias['idoso'].append(k)

    return faixas_etarias