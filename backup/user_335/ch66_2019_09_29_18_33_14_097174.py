def capitaliza (string):
    palavra = []
    primeira = string.title()
    palavra.append(primeira)
    i = 1
    while i < len(string):
        letra = string[i].lower()
        palavra.append(letra)
    return palavra