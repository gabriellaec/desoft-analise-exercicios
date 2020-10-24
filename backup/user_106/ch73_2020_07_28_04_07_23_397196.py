def remove_vogais(texto):
    novo = ''
    for i in texto:
        if not i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            novo.append(i)
    return novo