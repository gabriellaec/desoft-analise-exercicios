def separa_trios(lista):
    trios = []
    contador = 0
    while contador < len(lista):
        trio = lista[contador:(contador + 3)]
        trios.append(trio)
        contador += 3
    return trios