def conta_a(string):
    contador=0
    n=len(string)
    for i in range(0, len(string)):
        if string[i]=="a":
            contador+=1
    return contador
    