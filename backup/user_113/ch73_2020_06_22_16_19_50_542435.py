def remove_vogais(palavra):
    i = 0
    while i < len(palavra):
        if palavra[i] == 'a' or 'e' or 'i' or 'o' or 'u':
            del(palavra[i])
        else:
            i += 1