def remove_vogais(string):
    contador=0
    while contador < len(string):
        if string[contador]==["a","e","i","o","u"]:
            del string[contador]
    return string
        