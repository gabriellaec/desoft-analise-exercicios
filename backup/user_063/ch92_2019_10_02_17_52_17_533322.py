import functools
def simplifica_dict(dicionario):
    lista = list(functools.reduce(lambda x, y: x + y, dicionario.items()))
    lista_norep = set(lista)
    return lista_norep