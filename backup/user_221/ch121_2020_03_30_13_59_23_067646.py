def subtracao_de_listas(um, dois):
    i = 0
    j = 0
    while i < len(um) -1:
        while j < len(dois) - 1:
            if um[i] == dois[j]:
                del um[i]
                j = j + 1
            i = i + 1
    return um