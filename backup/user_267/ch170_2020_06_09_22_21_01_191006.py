
def apaga_repetidos(string):
    i = 0
    esc = ''
    while i < len(string):
        if string[i] in string:
            string[i] = "*"
        i += 1
    return string
