def estritamente_crescente(lista):
    return sorted(list(dict.fromkeys(lista)))
        