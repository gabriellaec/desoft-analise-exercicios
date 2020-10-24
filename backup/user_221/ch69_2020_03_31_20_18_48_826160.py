def junta_listas(original):
    i = 0
    soma = []
    while i < len(original):
        j = 0
        while j < len(original[i]):
            soma.append(original[i][j])
            j = j + 1
        i = i + 1
    return soma