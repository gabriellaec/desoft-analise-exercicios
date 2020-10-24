def remove_vogais(texto):
    novo = ''
    for i in texto:
        if not i == 'a' and i == 'e' and i == 'i' and i == 'o' and i == 'u':
            novo += i
    return novo