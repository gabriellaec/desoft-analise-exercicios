def agrupa_por_idade(nomes):
    dic = {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for i in nomes:
        if nomes[i] <= 11:
            nomes[i] = 'criança'
            dic.append(i)
        elif 12<=nomes[i]<=17:
            nomes[i] = 'adolescente'
            'adolescente'.append(i)
        elif 18<=nomes[i]<=59:
            nomes[i] = 'adulto'
            dic.append(i)
        elif nomes[i]>=60:
            nomes[i] = 'idoso'
            dic.append(i)
    print (dic)