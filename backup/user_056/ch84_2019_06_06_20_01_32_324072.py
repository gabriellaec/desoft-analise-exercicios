def inverte_dicionario(dicionario):
    invertido={}
    for nome,idade in dicionario.items():
        invertido[idade]=nome
    return invertido
        