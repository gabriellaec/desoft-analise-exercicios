def conta_a(string):
    vezes=0
    i=0
    while i<len(string): 
        if string[i]=="a":
            vezes+=1
            i+=1
        else:
            i+=1
    return vezes