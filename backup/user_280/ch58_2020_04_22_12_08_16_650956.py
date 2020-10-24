def conta_a(string):
    lista = []
    i=0
    while i < len(string):
        if string[i] == 'a':
            lista.append(i)
        i+=1
    return len(lista)