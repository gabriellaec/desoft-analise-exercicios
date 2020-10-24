def remove_vogais(palavra_com_vogais):
    t = 0
    psv = ""
    while t < len(palavra_com_vogais):
        if palavra_com_vogais[t] != 'a' and palavra_com_vogais[t] != 'e' and palavra_com_vogais[t] != 'i' and palavra_com_vogais[t] != 'o' and palavra_com_vogais[t] != 'u':
            psv += palavra_com_vogais[t]
        t += 1
    return psv
