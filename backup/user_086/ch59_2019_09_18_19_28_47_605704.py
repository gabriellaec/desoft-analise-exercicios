def conta_a(string):
    i=0
    apareceu=0
    while i<len(string):
        if string[i]=='a':
            apareceu+=1
        i+=1
    return apareceu
