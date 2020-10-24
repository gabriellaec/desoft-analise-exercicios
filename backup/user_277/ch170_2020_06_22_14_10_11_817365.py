def apaga_repetidos(string):
    string2 = ''
    for i in range(len(string)):
        if string[i] not in string2:
            string2 = string2 + string[i]
        else:
            string2 = string2 + '*'
    return string2