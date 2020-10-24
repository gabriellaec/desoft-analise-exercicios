def agrupa_por_idade(nomes):
    dic = {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for i in nomes:
        if nomes <= 11:
            i = 'criança'
            dic.append(i)
        elif '12'<=nomes<='17':
            i = 'adolescente'
            dic.append(i)
        elif '18'<=nomes<='59':
            i = 'adulto'
            dic.append(i)
        elif nomes>='60':
            i = 'idoso'
            dic.append(i)
    print (dic)