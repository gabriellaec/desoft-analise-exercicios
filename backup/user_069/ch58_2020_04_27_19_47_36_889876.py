def conta_a (string):
    i = 0
    ocorrencias = 0
    while i < len(string):
        if string[i] == 'a':
            ocorrencias += 1
        i += 1
    return ocorrencias