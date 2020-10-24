def todos_elementos(d):
    lista_chaves=list(d.keys())
    listas_valores=list(d.values())
    lista_todos=lista_chaves+listas_valores
    return lista_todos
def simplifica_dict(d):
    return list(dict.fromkeys(todos_elementos(d)))