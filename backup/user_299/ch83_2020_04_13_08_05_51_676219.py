def medias_por_inicial(dici):
    inicialenot = {}
    iniciaisusadas = []
    for nomes, notas in dici.items():
        inicial = nomes[0:1]
        if inicial not in iniciaisusadas:
            inicialenot[inicial] = notas
        elif inicial in iniciaisusadas:
            inicialenot[inicial] = (inicialenot[inicial]+notas)/2
    return inicialenot