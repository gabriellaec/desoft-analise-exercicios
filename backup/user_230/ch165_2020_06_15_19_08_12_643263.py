def mais_populoso (dicio):
    maior=0
    nome=0
    soma=0
    for estado,municipios in dicio.items():
        for municipio,hab in municipios.items():
            soma+=hab
        if soma>maior:
            maior=soma
            nome=estado
        soma=0
    return nome