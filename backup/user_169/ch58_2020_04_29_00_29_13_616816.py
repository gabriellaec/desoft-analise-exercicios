def conta_a(string):
    i=0
    lista=[]
    while i < len(string):
        if string[i] == 'a':
            lista.append(string[i])
        i+=1

    
    return len(lista)
