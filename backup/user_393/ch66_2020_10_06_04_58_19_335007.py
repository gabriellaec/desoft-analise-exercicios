def lista_sufixos(palavra):
    sufixos= []
    i= 0
    while i < len(palavra):
        sufixos.append(palavra[i:len(palavra)])
        i= i + 1
    return sufixos
