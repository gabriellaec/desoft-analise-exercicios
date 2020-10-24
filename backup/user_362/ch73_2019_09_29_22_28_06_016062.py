def remove_vogais(string):
    contador=0
    while contador < len(string):
        if string[contador]==["a"or"e"or"i"or"o"or"u"]:
            del string[contador]
    return string
        