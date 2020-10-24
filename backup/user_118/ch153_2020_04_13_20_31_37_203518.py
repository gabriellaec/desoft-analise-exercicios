def agrupa_por_idade(idade):
    dic={}
    for idade in dic:
        if idade >= 11:
            return 'crianca'
        elif 12<=idade<=17:
            return 'adolecente'
        elif 18<=idade<=59:
            return 'adulto'
        else:
            return 'idoso'