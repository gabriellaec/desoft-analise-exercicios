def agrupa_por_idade(dici):
    novodic = {}
    for nome, idade in dici.items():
        if idade < 12:
            if "criança" not in novodic.keys():
                novodic["criança"]= nome
            else:
                novodic["criança"] += nome
                
            
        if idade > 11 and idade < 18:
            if "adolescente" not in novodic.keys():
                novodic["adolescente"]=nome
            else:
                novodic["adolescente"] += nome
            
        if idade > 17 and idade < 60:
            if "adulto" not in novodic.keys():
                novodic["adulto"]= nome
                 else:
                novodic["adulto"] += nome
          
        if idade > 59:
             if "idoso" not in novodic.keys():
                novodic["idoso"]=nome
                 else:
                novodic["idoso"] += nome
    return novodic
  