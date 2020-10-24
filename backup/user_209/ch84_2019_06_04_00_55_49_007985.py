def inverte_dicionario (dicobas,diceras):
    dicobas = {}
    diceras = {}
    for nome,idade in dicobas:
        for inverso in dicobas.items():
            inverso = inverso[::-1]
            dicoceras.append(inverso)
    return diceras