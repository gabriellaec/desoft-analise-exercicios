def conta_a(string):
    i=0
    soma=0
    while i < len(string):
        if string[i] == "a":
            soma+= string[i]
        i+=1
    return soma
