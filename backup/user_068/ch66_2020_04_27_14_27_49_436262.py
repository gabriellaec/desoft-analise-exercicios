def  lista_sufixos(palavra):
    a = []
    foi i in range(len(palavra)):
        t = palavra[i:-1]
        a.append(t)
    return a