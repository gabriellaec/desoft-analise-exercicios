def verifica_progressao(lista):
    i = 0 
    while i < len(lista):
        if i[1] - i[0] == i[3] - i[2]:
            return "PA"
        elif i[1]/i[0] == i[3]/i[2]:
            return "PG"
        else:
            return "AG"
        i += 1