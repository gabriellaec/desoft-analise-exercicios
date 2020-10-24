def mais_populoso (dicio):
    maior=0
    nome=0
    soma=0
    for estado in dicio:
        for municipio,hab in estado.items():
            soma+=hab
        if soma>maior:
            maior=soma
            nome=estado
        soma=0
    return nome