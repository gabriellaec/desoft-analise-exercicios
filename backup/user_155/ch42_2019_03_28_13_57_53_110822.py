def quantos_uns(string):
    string = str(string)
    i = 0
    uns = 0 
    while i < len(string):
        if string[i] == '1':
            uns +=1
        i+=1
    return uns