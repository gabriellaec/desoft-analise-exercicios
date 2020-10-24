def inverte_dicionario(dicionario):
    invertido = {}
    for idade in dicionario.values():
        invertido[idade] = []
    for nome,idade in dicionario.items():
        invertido[idade].append(nome)
    return invertido