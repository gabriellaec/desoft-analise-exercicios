#igual ao da video aula

def conta_letras(string):
    dict = {}
    for i in string:
        if i not in dict:
            dict[i] = 1
        elif i in dict:
            dict[i] += 1
    return dict