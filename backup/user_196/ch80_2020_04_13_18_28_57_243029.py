from collections import ChainMap
def interseccao_chaves(dic1,dic2):
    lista = []
    dicionariofinal = ChainMap({}, dic2,dic1)
    for a,b in dicionariofinal.items():
        lista.append(a)
        lista.append(b)
    return lista
