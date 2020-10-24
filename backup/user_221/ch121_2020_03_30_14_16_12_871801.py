def subtracao_de_listas(um, dois):
    i = 0
    j = 0
    while i < len(um):
        while j < len(dois):
            if um[i] == dois[j]:
                del um[i]
                i = i - 1
            j = j + 1
        i = i + 1
    return um