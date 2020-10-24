def lista_caracteres(string):
    j = []
    k=[]
    for i in range(len(string)):
        j.append(string[i])
        if string[i] not in j:
            k = string.split()
    return k