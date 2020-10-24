def pos_arroba(string):
    i=0
    while i<len(string):
        if string[i]=='@':
            resultado=i+1
            break
        i+=1
    return resultado