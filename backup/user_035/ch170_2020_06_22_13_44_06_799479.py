def apaga_repetidos(texto):
    string = ""
    for i in texto:
        if i in string:
            string += "*"
        else:
            string += i
    return string