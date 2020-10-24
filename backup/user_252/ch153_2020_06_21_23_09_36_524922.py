def agrupa_por_idade(dicio):
    agrupa={'criança': [], 'aolescente': [], 'adulto': [], 'idoso': []}
    for nome, idade in dicio.items():
        if idade <= 11:
            agrupa['criança'].append(nome)
        elif idade >= 12 and idade <=17:
            agrupa['adolescente'].append(nome)
        elif idade >= 18 and idade <= 59:
            agrupa['adulto'].append(nome)
        elif idade > 59:
            agrupa['idoso'].append(nome)
    return agrupa
            
        
        
            