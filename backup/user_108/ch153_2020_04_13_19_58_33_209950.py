def agrupa_por_idade(pessoas):
    idades = {}
    for nome,idade in pessoas.items():
        chave = "idoso"
        if idade <= 11:
            chave = "criança"
        elif idade 12 <= idade <= 17:
        idades[idade] = idades.get(idade,[])
        idades[idade].append(nome)
    return idades