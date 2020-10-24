
def remove_vogais(palavra_com_vogais):
    t = 0
    while t < len(palavra_com_vogais):
        if 'a'  == palavra_com_vogais[t] or 'e' == palavra_com_vogais[t] or 'i'  == palavra_com_vogais[t] or 'o' == palavra_com_vogais[t] or 'u' == palavra_com_vogais[t]:
            palavra_com_vogais = palavra_com_vogais.replace(palavra_com_vogais[t],"")
        t += 1
    return palavra_com_vogais

