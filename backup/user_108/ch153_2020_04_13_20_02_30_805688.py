def agrupa_por_idade(pessoas):
    idades = {}
    for nome,idade in pessoas.items():
        chave = "idoso"
        if idade <= 11:
            chave = "criança"
        elif 12 <= idade <= 17:
            chave = "adolescente"
        elif 18 <= idade <= 59:
            chave = "adulto"
        idades[chave] = idades.get(chave,[])
        idades[chave].append(nome)
    return idades