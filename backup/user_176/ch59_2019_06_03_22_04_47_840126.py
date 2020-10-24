def conta_a(string):
    aparece_a = 0
    i = 0
    while i<len(string):
        if string[i]=='a':
        aparece_a+=1
        i+=1
    return aparece_a