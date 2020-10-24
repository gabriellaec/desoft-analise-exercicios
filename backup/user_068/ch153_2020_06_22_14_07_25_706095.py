def agrupa_por_idade(dici):
    novodic = {}
    for nome, idade in dici.items():
        if idade < 12:
            if "criança" not in novodic.keys():
                novodic["criança"]= [nome]
            elif 'criança' in novodic.keys():
                novodic["criança"].append(nome)
                
            else:
                novodic["adolescente"]= []
        if idade > 11 and idade < 18:
            if "adolescente" not in novodic.keys():
                novodic["adolescente"]= [nome]
            elif 'adolescente' in novodic.keys():
                novodic["adolescente"].append(nome)
            else:
                novodic["adolescente"]= []
            
        if idade > 17 and idade < 60:
            if "adulto" not in novodic.keys():
                novodic["adulto"]= [nome]
            elif 'adulto' in novodic.keys():
                novodic["adulto"].append(nome)
            else:
                novodic["adolescente"]= []  
        if idade > 59:
            if "idoso" not in novodic.keys():
                novodic["idoso"]= [nome]
            elif 'idoso' in novodic.keys():
                novodic["idoso"].append(nome)
            else:
                novodic["adolescente"]= []
    return novodic
  