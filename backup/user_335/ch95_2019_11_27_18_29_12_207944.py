def mais_populoso (dicionario):
    estado_mp = 0 
    soma_mp = 0

    for estado,municipio in dicionario.items():
        somahab = 0
        for muni, habitantes in municipio.items():
            somahab += habitantes

        if somahab > soma_mp:
            soma_mp = somahab
            estado_mp = estado

    return estado_mp