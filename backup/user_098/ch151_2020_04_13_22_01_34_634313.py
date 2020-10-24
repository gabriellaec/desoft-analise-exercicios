def estritamente_crescente(list):
    return all(a < b for a, b in zip(list, list[1:]))


def estritamente_decrescente(list):
    return all(a > b for a, b in zip(list, list[1:]))


def classifica_lista(list):
    if len(list) > 2:
        if estritamente_crescente(list):
            return 'crescente'
        elif estritamente_decrescente(list):
            return 'decrescente'
        else:
            return 'nenhum'
    else:
        return 'nenhum'