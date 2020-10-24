def agrupa_por_idade(pessoas):
    idades = {}
    for nome,idade in pessoas.items():
        idades[idade] = idades.get(idade,[])
        idades[idade].append(nome)
    return idades