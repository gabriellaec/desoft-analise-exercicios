def conta_a(string):
    resultado=0
    i=0
    while i<len(string):
        if string[i]=='a':
            resultado+=1
        i+=1
    return resultado