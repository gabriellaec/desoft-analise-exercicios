def agrupa_por_idade(dici):
    novodic = {}
    for nome, idade in dici.items():
        if idade < 12:
            novodic["criança"] = nome
            
        if idade > 11 and idade < 18:
            novodic["adolescente"] = nome
            
        if idade > 17 and idade < 60:
            novodic["adulto"] = nome
          
        if idade > 59:
            novodic["idoso"] = nome
    return novodic