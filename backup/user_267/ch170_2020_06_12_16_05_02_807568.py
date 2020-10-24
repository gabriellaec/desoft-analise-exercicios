def apaga_repetidos(string):
    esc = ''
    a = 0
    for i in range(len(string)):
        while a < len(string):
            if string[i] == string[a]:
                esc += "*"
            else:
                esc += string[i]
            a += 1
    return esc

