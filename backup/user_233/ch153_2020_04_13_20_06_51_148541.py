def agrupa_por_idade(dict_idades):
    
    dict_pessoas_por_faixa_etaria = {
        'criança': [],
        'adolescente': [],
        'adulto': [],
        'idoso': []
        }
    
    for pessoa in dict_idades.keys():
        
        if lista_idades[pessoa] <= 11:
            dict_pessoas_por_faixa_etaria['criança'].append(pessoa)
        elif lista_idades[pessoa] <= 17:
            dict_pessoas_por_faixa_etaria['adolescente'].append(pessoa)
        elif lista_idades[pessoa] <= 59:
            dict_pessoas_por_faixa_etaria['adulto'].append(pessoa)
        else:
            dict_pessoas_por_faixa_etaria['idoso'].append(pessoa)
    
    return dict_pessoas_por_faixa_etaria
        
        
        
        