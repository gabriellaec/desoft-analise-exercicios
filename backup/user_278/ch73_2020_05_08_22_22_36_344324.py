def remove_vogais (texto):
    vogais = ["a","e","i","o","u"]
    for i in texto:
        if i in vogais:
            texto = texto.replace(i,'')
    return texto