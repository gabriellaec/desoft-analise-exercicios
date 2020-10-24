def remove_vogais(txt):
    i = 0
    while i < (len(txt)):
        if (txt[i] == 'a') or (txt[i] == 'e') or (txt[i] == 'i') or (txt[i] == 'o') or (txt[i] == 'u'):
            txt[i] = ''
        i += 1
    return txt