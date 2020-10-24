def remove_vogais (texto):
    vogais = ["a","e","i","o","u"]
    for v in range (len(texto)):
        if v in vogais:
            texto.remove(v) 
    return texto