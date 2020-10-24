def remove_vogais (string):
    i = 0
    b = "aeiou"
    while i < len(b):
        a = string.lower()
        resultado = a.replace(b[i], "")
        i += 1
    return resultado
        
    