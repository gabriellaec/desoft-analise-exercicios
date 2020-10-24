def conta_a(string):
    aparece_a = []
    i = 0
    while i<len(string):
        if 'a' in string:
            aparece_a.append(string[i])
        i+=1
    return len(aparece_a)