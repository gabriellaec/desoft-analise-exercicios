def agrupa_por_idade(nomes):
    gui = {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for i in nomes:
        if nomes[i] <= 11:
            nomes[i] = 'criança'
            gui.append(nomes[i])
        elif 12<=nomes[i]<=17:
            nomes[i] = 'adolescente'
            adolescente.append(nomes[i])
        elif 18<=nomes[i]<=59:
            nomes[i] = 'adulto'
            gui.append(nomes[i])
        elif nomes[i]>=60:
            nomes[i] = 'idoso'
            gui.append(nomes[i])
    print (dic)