def subtracao_de_listas(um, dois):
    i = 0
    j = 0
while i < len(um) and j < len(dois):
    while um[i] == dois[j]:
        del um[i]
        j = j + 1
    i = i + 1
return um