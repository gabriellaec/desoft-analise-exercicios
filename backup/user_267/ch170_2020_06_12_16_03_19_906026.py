def apaga_repetidos(string):
    esc = ''
    for i in range(len(string)):
        if string[i] == string[i-1]:
            esc += "*"
        else:
            esc += string[i]
    return esc

