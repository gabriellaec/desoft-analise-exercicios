def remove_vogais(texto):
    i = 0
    while i <= (len(texto)-1):
        if texto[i] == 'a' or texto[i] == 'e' or texto[i] == 'i' or texto[i] == 'o' or texto[i] == 'u':
            del texto[i]
    return texto