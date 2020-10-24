def conta_a(string):
    i=0
    apareceu=0
    while i<len(string):
        letra=string[i]
        if letra in string:
            apareceu+=1
        i+=1
