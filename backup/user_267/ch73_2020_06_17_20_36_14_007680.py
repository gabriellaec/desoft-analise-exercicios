def remove_vogais(txt):
    i = 0
    novo_txt = ''
    while i < (len(txt)):
        if not ((txt[i] == 'a') or (txt[i] == 'e') or (txt[i] == 'i') or (txt[i] == 'o') or (txt[i] == 'u')):
            novo_txt += txt[i]
        i += 1
    return novo_txt