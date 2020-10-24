def apaga_repetidos(string):
    esc = ''
    a = 0
    for i in range(len(string)):
        if string[i] in esc:
            esc += "*"
        else:
            esc += string[i]
    return esc

