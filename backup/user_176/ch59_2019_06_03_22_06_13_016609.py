def conta_a(string):
    i=0
    aparece=0
    while i<len(string):
        if string[i]=='a':
            aparece+=1
        i+=1
    return aparece