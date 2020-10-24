def conta_a (string):
    i=0
    número_de_as = 0
    while i < len(string):
        if string[i] == 'a':
            número_de_as+=1
        i+=1
    return número_de_as
        