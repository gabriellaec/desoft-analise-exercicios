def remove_vogais(texto):
    for i in texto:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            del i
    return texto