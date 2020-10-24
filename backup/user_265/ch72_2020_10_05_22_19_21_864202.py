def lista_caracteres(palavra):
    j = 0
    nova = [palavra[0]]

    while j < len(palavra):
            if palavra[0] == palavra[j]:
                j += 1
            else:
                nova.append(palavra[j])
                j += 1
    
    return nova
    