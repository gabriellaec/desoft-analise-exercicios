def remove_vogais(texto):
    x = 0
    while x < len(texto):
        if texto[x] == 'a' or texto[x] == 'e' or texto[x] == 'i' or texto[x] == 'o' or texto[x] == 'u':
            del texto[x]
        x += 1
    return texto