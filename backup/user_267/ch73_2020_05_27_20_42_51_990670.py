def remove_vogais(texto):
    i = 0
    while i < (len(texto)):
        if texto[i] == 'a' or texto[i] == 'e' or texto[i] == 'i' or texto[i] == 'o' or texto[i] == 'u':
            del texto[i]
        i += 1
    return texto