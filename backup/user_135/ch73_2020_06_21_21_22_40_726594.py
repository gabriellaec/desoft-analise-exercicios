def remove_vogais(texto):
    return texto.translate({ord('a'): None, ord('e'): None, ord('i'): None, ord('o'): None, ord('u'): None})